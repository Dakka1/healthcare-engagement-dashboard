Healthcare Engagement Dashboard

This project provides a simple full stack system for viewing physician messages and running compliance classification. It includes a Python FastAPI backend and a React frontend. The goal is to load physician and message data, expose clean backend APIs, and display results in a small UI.

Setup instructions

Backend setup

The backend uses FastAPI and SQLite.
	1.	Navigate to the project root
cd healthcare-engagement-dashboard
	2.	Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
	3.	Install dependencies
pip install -r backend/requirements.txt
	4.	Run the backend
uvicorn backend.main:app --reload

The backend will be available at
http://localhost:8000

Backend Docker setup
	1.	Build the backend image
docker build -t healthcare-backend .
	2.	Start the backend container
docker run -p 8000:8000 healthcare-backend

Frontend setup
	1.	Navigate to frontend
cd frontend
	2.	Install dependencies
npm install
	3.	Run the frontend
npm start

The frontend will be available at
http://localhost:3000

API endpoints

GET /physicians

Returns physician records with optional filtering.

Query parameters
state
specialty

Example
GET /physicians?state=NY&specialty=Oncology

GET /messages

Returns messages with filtering.

Query parameters
physician_id
start_date
end_date

Example
GET /messages?physician_id=101&start_date=2025-08-01&end_date=2025-08-20

POST /classify/{message_id}

Runs compliance classification on a message using the provided JSON rules.

Example
POST /classify/10006

Returns
triggered_rules
each rule includes id name action and requires_append if present

Short description of design

The backend is built with FastAPI. At startup it loads physicians and messages from CSV into an SQLite database. It exposes three endpoints for filtering physicians filtering messages and classifying messages. Message classification reads compliance_policies.json and checks a message text for any matching keywords. Request latency is logged for each backend call.

The frontend is a minimal React application. It allows the user to enter a physician id search for messages and view a table containing timestamp topic and sentiment. Each row includes a Classify button that triggers the backend and displays the resulting rule matches in a modal.

The project meets the requirements by providing physician filtering message filtering including date ranges and a working classifier that shows triggered compliance rules.