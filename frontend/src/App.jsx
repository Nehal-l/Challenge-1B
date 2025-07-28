import React, { useState } from "react";
import FileUpload from "./components/FileUpload";
import PersonaForm from "./components/PersonaForm";
import JsonDisplay from "./components/JsonDisplay";
import "./App.css";

const App = () => {
  const [files, setFiles] = useState([]);
  const [persona, setPersona] = useState("");
  const [job, setJob] = useState("");
  const [jsonData, setJsonData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState("");

  const handleAnalyze = async () => {
    if (!files.length || !persona || !job) {
      setErrorMsg("Please upload at least one file and fill in all fields.");
      return;
    }

    const formData = new FormData();
    files.forEach((file) => formData.append("documents", file));
    formData.append("persona", persona);
    formData.append("job", job);

    setLoading(true);
    setErrorMsg("");
    setJsonData(null);

    try {
      const res = await fetch("http://localhost:5000/analyze", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.error || "Server Error");
      }

      const data = await res.json();
      setJsonData(data);
    } catch (err) {
      console.error("Error during fetch:", err.message);
      setErrorMsg("Analysis failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>Persona-Based PDF Intelligence</h1>

      <FileUpload files={files} setFiles={setFiles} />
      {files.length > 0 && <p>{files.length} PDF(s) selected</p>}

      <PersonaForm
        persona={persona}
        setPersona={setPersona}
        job={job}
        setJob={setJob}
      />

      <button onClick={handleAnalyze} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>

      {errorMsg && <p className="error">{errorMsg}</p>}
      {loading && (
        <p>
          Analyzing {files.length} document{files.length > 1 ? "s" : ""}...
        </p>
      )}
      {!loading && jsonData && <JsonDisplay jsonData={jsonData} />}
    </div>
  );
};

export default App;
