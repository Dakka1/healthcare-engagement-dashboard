import React, { useState } from "react";

function Filters({ onSearch }) {
  const [physicianId, setPhysicianId] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    if (!physicianId.trim()) {
      return;
    }
    onSearch(physicianId.trim());
  }

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: "flex", gap: "0.75rem", alignItems: "flex-end" }}
    >
      <div style={{ display: "flex", flexDirection: "column" }}>
        <label htmlFor="physicianId" style={{ marginBottom: "0.25rem" }}>
          Physician id
        </label>
        <input
          id="physicianId"
          type="number"
          value={physicianId}
          onChange={(e) => setPhysicianId(e.target.value)}
          placeholder="For example 101"
          style={{ padding: "0.4rem 0.6rem" }}
        />
      </div>
      <button
        type="submit"
        style={{
          padding: "0.45rem 0.9rem",
          cursor: "pointer",
          borderRadius: "4px",
          border: "1px solid #333",
          backgroundColor: "#222",
          color: "#fff"
        }}
      >
        Search
      </button>
    </form>
  );
}

export default Filters;