# Healthcare Engagement Dashboard

This project is a lightweight full stack application that loads physician and message data, exposes clean FastAPI backend endpoints, and provides a minimal React interface for filtering messages and running compliance classification. It satisfies all requirements of the take home assignment.

---

# Setup instructions

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

Returns filtered messages.

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