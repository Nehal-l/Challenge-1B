# 📄 Challenge Round 1B: Persona-Driven Document Intelligence

A full-stack AI-powered application that extracts structured outlines and generates persona-driven summaries from PDF documents using a lightweight local LLaMA-based model.

---

## 🚀 Features

- Upload PDF files from the frontend.
- Extract **title**, **headings (H1, H2, H3)** with **page numbers**.
- Generate **personalized summaries** based on a given **persona** and **task**.
- Runs completely **offline** using the `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` model via `llama-cpp-python`.
- Beautiful frontend interface with animated themes, hover effects, and clean layout.

---

## 🗂️ Project Structure

Challenge-1B/
├── backend/
│ ├── app.py
│ ├── pdf_utils.py
│ ├── prompt_builder.py
│ ├── model/
│ │ └── tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf
│ └── requirements.txt
├── frontend/
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ ├── FileUpload.jsx
│ │ │ ├── SummaryDisplay.jsx
│ │ │ └── OutlineDisplay.jsx
│ │ ├── App.jsx
│ │ └── App.css
│ └── package.json
└── README.md

yaml

---

## 🧠 Model Info

We use the [TinyLLaMA 1.1B Chat](https://huggingface.co/csakyo/tinyllama-1.1b-chat-v1.0-GGUF) model (`Q4_K_M` quantized GGUF format), which is:

- 🔹 Lightweight (~680MB)
- 🔹 Fully compatible with `llama-cpp-python`
- 🔹 Efficient for CPU inference
- 🔹 Ideal for offline summarization tasks

Model must be manually downloaded and placed in:

backend/model/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf

yaml

---

## ⚙️ Backend Setup (Flask + llama-cpp)

### 1. Install Python dependencies

```bash
cd backend
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux

pip install -r requirements.txt
