from flask import Flask, request, jsonify
from flask_cors import CORS
from llama_cpp import Llama
from datetime import datetime
import os
import tempfile
from pdf_utils import extract_text_by_page
from prompt_builder import build_prompt

app = Flask(__name__)
CORS(app)

model_path = os.path.join("model", "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf")

# Load TinyLLaMA with optimized parameters
llm = Llama(
    model_path=model_path,
    n_ctx=1024,
    n_threads=6,
    n_batch=64,
    low_cpu_mem_usage=True,
    verbose=False
)

@app.route("/analyze", methods=["POST"])
def analyze_documents():
    files = request.files.getlist("documents")
    persona = request.form.get("persona")
    task = request.form.get("job")

    if not files or not persona or not task:
        return jsonify({"error": "Missing files or form data"}), 400

    print(f"[INFO] Analyzing {len(files)} files...")

    metadata = {
        "input_documents": [f.filename for f in files],
        "persona": persona,
        "job_to_be_done": task,
        "timestamp": datetime.now().isoformat()
    }

    extracted_sections = []
    sub_section_analysis = []

    for pdf_file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            pdf_file.save(tmp.name)
            pages = extract_text_by_page(tmp.name)

        for i, text in enumerate(pages[:3]):  # ✅ Max 3 pages
            if not text.strip():
                continue

            section_text = text.strip().replace("\n", " ")[:600]
            if len(section_text.split()) < 25:
                continue  # Skip pages with too little content

            prompt = build_prompt(persona, task, section_text)

            try:
                res = llm(prompt, max_tokens=160, stop=["\n\n", "###"])
                output = res["choices"][0]["text"].strip()

                # Retry with shorter text if model gave nothing
                if not output:
                    retry_prompt = build_prompt(persona, task, section_text[:300])
                    res = llm(retry_prompt, max_tokens=120, stop=["\n\n", "###"])
                    output = res["choices"][0]["text"].strip()
            except Exception as e:
                print(f"[ERROR] LLM failed on page {i+1}: {e}")
                output = ""
            
            # Always return summary (even fallback)
            if "relevant" in output.lower() or len(output) > 30:
                extracted_sections.append({
                    "document": pdf_file.filename,
                    "page_number": i + 1,
                    "section_title": section_text[:80],
                    "importance_rank": 1
                })

            sub_section_analysis.append({
                "document": pdf_file.filename,
                "refined_text": output if output else "Summary not available.",
                "page_number": i + 1
            })

    return jsonify({
        "metadata": metadata,
        "extracted_sections": extracted_sections,
        "sub_section_analysis": sub_section_analysis
    })

if __name__ == "__main__":
    os.environ['FLASK_RUN_FROM_CLI'] = 'false'
    app.run(debug=False, port=5000)
