import React from "react";

function MessageRow({ message, onClassify }) {
  const timestamp = new Date(message.timestamp).toLocaleString();

  return (
    <tr>
      <td style={{ padding: "0.5rem 0" }}>{timestamp}</td>
      <td style={{ padding: "0.5rem 0" }}>{message.topic}</td>
      <td style={{ padding: "0.5rem 0" }}>{message.sentiment}</td>
      <td style={{ padding: "0.5rem 0" }}>
        <button
          type="button"
          onClick={() => onClassify(message)}
          style={{
            padding: "0.3rem 0.7rem",
            cursor: "pointer",
            borderRadius: "4px",
            border: "1px solid #0a6",
            backgroundColor: "#0a6",
            color: "#fff"
          }}
        >
          Classify
        </button>
      </td>
    </tr>
  );
}

export default MessageRow;