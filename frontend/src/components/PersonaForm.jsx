import React from "react";

const PersonaForm = ({ persona, setPersona, job, setJob }) => (
  <div className="form-box">
    <input
      type="text"
      placeholder="Enter Persona"
      value={persona}
      onChange={(e) => setPersona(e.target.value)}
    />
    <textarea
      placeholder="Enter Job to be Done"
      value={job}
      onChange={(e) => setJob(e.target.value)}
    />
  </div>
);

export default PersonaForm;
