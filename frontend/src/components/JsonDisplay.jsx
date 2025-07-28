import React from "react";

const JsonDisplay = ({ jsonData }) => {
  const prettyJson = JSON.stringify(jsonData, null, 2);

  return (
    <div className="json-container">
      <pre>{prettyJson.replace(/\\n/g, "\n")}</pre>
    </div>
  );
};

export default JsonDisplay;
