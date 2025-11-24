import React from "react";

function ClassifyModal({ open, onClose, classification, loading }) {
  if (!open) {
    return null;
  }

  return (
    <div
      style={{
        position: "fixed",
        inset: 0,
        backgroundColor: "rgba(0,0,0,0.35)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        zIndex: 1000
      }}
    >
      <div
        style={{
          backgroundColor: "#fff",
          padding: "1.25rem 1.5rem",
          borderRadius: "8px",
          maxWidth: "540px",
          width: "100%",
          boxShadow: "0 4px 16px rgba(0,0,0,0.25)"
        }}
      >
        <div
          style={{
            display: "flex",
            justifyContent: "space-between",
            marginBottom: "0.75rem"
          }}
        >
          <button
            type="button"
            onClick={onClose}
            style={{
              border: "none",
              background: "transparent",
              fontSize: "1.1rem",
              cursor: "pointer"
            }}
          >
            ×
          </button>
        </div>

        {loading && <p>Classifying message</p>}

        {!loading && classification && (
          <>

            <h3 style={{ marginTop: 0 }}>Triggered rules</h3>
            {classification.triggered_rules &&
            classification.triggered_rules.length > 0 ? (
              <ul>
                {classification.triggered_rules.map((rule) => (
                  <li key={rule.id} style={{ marginBottom: "0.4rem" }}>
                    <strong>{rule.id}</strong> {rule.name}
                    {rule.action && (
                      <span>
                        {" "}
                        action: <em>{rule.action}</em>
                      </span>
                    )}
                    {rule.requires_append && (
                      <div>Requires append: {rule.requires_append}</div>
                    )}
                  </li>
                ))}
              </ul>
            ) : (
              <p>No compliance rules matched this message.</p>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default ClassifyModal;