# Healthcare Engagement Dashboard

This project is a small full stack application that loads physicians and message data, exposes clean backend API endpoints, and provides a minimal React interface to filter messages and run compliance classification. It satisfies all requirements of the take home assignment.

---

# Setup instructions

## Option A: Run locally (recommended)

### Backend

1. Navigate to the project root  
   `cd healthcare-engagement-dashboard`

2. Create and activate a virtual environment  
   `python3 -m venv venv`  
   `source venv/bin/activate`

3. Install backend dependencies  
   `pip install -r backend/requirements.txt`

4. Start the backend  
   `uvicorn backend.main:app --reload`

Backend runs at:  
`http://localhost:8000`

### Frontend

1. Navigate to frontend  
   `cd frontend`

2. Install dependencies  
   `npm install`

3. Run the frontend  
   `npm start`

Frontend runs at:  
`http://localhost:3000`

---

## Option B: Run using the backend Dockerfile

1. From the project root:  
   `docker build -t healthcare-backend .`

2. Run the backend container:  
   `docker run -p 8000:8000 healthcare-backend`

Frontend must still be run manually with:  
`cd frontend && npm start`

---

# API Endpoints

## `GET /physicians`

Returns physician records with optional filters.

### Query parameters  
`state`  
`specialty`

### Example  
`GET /physicians?state=NY&specialty=Oncology`

---

## `GET /messages`

Returns filtered message records.

### Query parameters  
`physician_id`  
`start_date`  
`end_date`

### Example  
`GET /messages?physician_id=101&start_date=2025-08-01&end_date=2025-08-20`

---

## `POST /classify/{message_id}`

Classifies a message using rules in `compliance_policies.json`.

### Example  
`POST /classify/10006`

### Returns  
A list of triggered compliance rules.

---

# Short description of design

The backend is built with FastAPI. At startup it loads physicians and messages from CSV files into an SQLite database. It provides three core endpoints for filtering physicians, filtering messages by physician and date range, and classifying a message. Compliance rules are loaded from a JSON file and matched against message text. The backend logs request latency for every call.

The frontend is a simple React application that meets the assignment requirements. It provides:

• A field to search messages by physician id  
• A table showing each message’s timestamp, topic, and sentiment  
• A “Classify” button that opens a modal showing any triggered compliance rules

The design is intentionally lightweight, meeting the exact assignment criteria with clear separation between backend and frontend code.