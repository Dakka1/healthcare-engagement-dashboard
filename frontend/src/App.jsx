import React, { useState } from "react";
import Filters from "./components/filters";
import MessageRow from "./components/message";
import ClassifyModal from "./components/classifyModal";
import { fetchMessages, classifyMessage } from "./api";

function App() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedMessage, setSelectedMessage] = useState(null);
  const [classification, setClassification] = useState(null);
  const [classifyLoading, setClassifyLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSearch(physicianId) {
    try {
      setError("");
      setLoading(true);
      const data = await fetchMessages(physicianId);
      setMessages(data);
    } catch (err) {
      console.error(err);
      setMessages([]);
      setError("Could not load messages");
    } finally {
      setLoading(false);
    }
  }

  async function handleClassify(message) {
    try {
      setSelectedMessage(message);
      setClassification(null);
      setClassifyLoading(true);
      const result = await classifyMessage(message.id);
      setClassification(result);
    } catch (err) {
      console.error(err);
      setClassification({
        message_id: message.id,
        message_text: "Error while classifying message",
        triggered_rules: []
      });
    } finally {
      setClassifyLoading(false);
    }
  }

  function closeModal() {
    setSelectedMessage(null);
    setClassification(null);
    setClassifyLoading(false);
  }

  return (
    <div
      style={{
        fontFamily: "system-ui, sans-serif",
        padding: "1.5rem",
        maxWidth: "960px",
        margin: "0 auto"
      }}
    >
      <header style={{ marginBottom: "1.5rem" }}>
        <h1>Healthcare engagement dashboard</h1>
        <p style={{ color: "#555" }}>
          Search messages by physician id and run compliance classification.
        </p>
      </header>

      <section style={{ marginBottom: "1rem" }}>
        <Filters onSearch={handleSearch} />
      </section>

      {error && (
        <p style={{ color: "red", marginBottom: "0.5rem" }}>{error}</p>
      )}

      <section>
        {loading ? (
          <p>Loading messages</p>
        ) : (
          <table
            style={{
              width: "100%",
              borderCollapse: "collapse",
              marginTop: "0.5rem"
            }}
          >
            <thead>
              <tr>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Id
                </th>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Physician
                </th>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Timestamp
                </th>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Topic
                </th>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Sentiment
                </th>
                <th style={{ textAlign: "left", borderBottom: "1px solid #ccc" }}>
                  Compliance
                </th>
              </tr>
            </thead>
            <tbody>
              {messages.length === 0 ? (
                <tr>
                  <td colSpan={6} style={{ padding: "0.75rem 0" }}>
                    No messages yet. Search by physician id.
                  </td>
                </tr>
              ) : (
                messages.map((m) => (
                  <MessageRow
                    key={m.id}
                    message={m}
                    onClassify={handleClassify}
                  />
                ))
              )}
            </tbody>
          </table>
        )}
      </section>

      <ClassifyModal
        open={Boolean(selectedMessage)}
        classification={classification}
        loading={classifyLoading}
        onClose={closeModal}
      />
    </div>
  );
}

export default App;