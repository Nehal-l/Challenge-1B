import React from "react";

const FileUpload = ({ files, setFiles }) => {
  return (
    <div className="upload-box">
      <input
        type="file"
        multiple
        onChange={(e) => setFiles([...e.target.files])}
      />
    </div>
  );
};

export default FileUpload;
