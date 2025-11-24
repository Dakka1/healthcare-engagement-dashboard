# Healthcare Engagement Dashboard

This project is a lightweight full stack application that loads physician and message data, exposes clean FastAPI backend endpoints, and provides a minimal React interface for filtering messages and running compliance classification.

---

# Setup instructions

```
# Prerequisites

Before running the project, ensure the following are installed on your system:

• **Docker Desktop**
  Required to build and run the backend container.

• **Node.js and npm**
  Required to run the React frontend using `npm run frontend`.

### Windows users  
This project works on Windows without issues. You can run everything using either of these methods:  
• Install and run Docker Desktop  
• Install Node.js and npm (both fully supported on Windows)  
• Use Git Bash to run run.sh

If you prefer not to use run.sh, you can run the Docker commands manually on Windows, Linux, and Mac:

```
docker build -t healthcare-backend .
docker stop healthcare-backend || true
docker rm healthcare-backend || true
docker run -d --name healthcare-backend -p 8000:8000 healthcare-backend
```
```

## Run using Docker

The backend runs entirely inside Docker. (we can run locally too but cleaner in docker)

### Backend

From the project root, run:

```
./run.sh
```

The run.sh script performs the following steps:

• Builds the backend Docker image
• Stops and removes any existing backend container
• Starts a new backend container on port 8000

Backend is available at:
```
http://localhost:8000
```

### Frontend

To run the React frontend from the project root:

```
npm run frontend
```

This command automatically:
• Navigates into the frontend folder  
• Installs all required npm packages via npm install 
• Starts the React development server  via npm start

The app will be available at:
```
http://localhost:3000
```

---

# API Endpoints

## GET /physicians

Returns physician records with optional filters.

### Query parameters
• state  
• specialty  

### Example
```
GET /physicians?state=NY&specialty=Oncology
```

---

## GET /messages

Returns filtered messages with optional filters.

### Query parameters
• physician_id  
• start_date  
• end_date  

### Example
```
GET /messages?physician_id=101&start_date=2025-08-01&end_date=2025-08-20
```

---

## POST /classify/{message_id}

Classifies a message using the compliance rules defined in compliance_policies.json.

### Example
```
POST /classify/10006
```

### Returns
A list of triggered compliance rules.

---

# Short description of design

The backend is built with FastAPI. At startup it loads physicians and messages from CSV files into an SQLite database. It exposes three core endpoints:

• Filter physicians  
• Filter messages by physician and date range  
• Classify a message against compliance rules  

Each request is logged with latency timing.

The frontend is a minimal React application that provides:

• Search messages by physician id  
• A table showing timestamp, topic, and sentiment  
• A “Classify” button per row that opens a modal displaying triggered rules  

The design is intentionally simple, meeting the assignment requirements while maintaining clean separation of backend and frontend responsibilities.
