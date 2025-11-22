export const API_URL = "http://localhost:8000";

export async function fetchMessages(physicianId) {
  const params = new URLSearchParams();
  if (physicianId) {
    params.append("physician_id", physicianId);
  }

  const res = await fetch(`${API_URL}/messages?${params.toString()}`);
  if (!res.ok) {
    throw new Error("Failed to fetch messages");
  }
  return res.json();
}

export async function classifyMessage(id) {
  const res = await fetch(`${API_URL}/classify/${id}`, {
    method: "POST",
    headers: { accept: "application/json" }
  });

  if (!res.ok) {
    throw new Error("Failed to classify message");
  }
  return res.json();
}