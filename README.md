
# ChocHouseProject

A management system for ChocHouse to handle categories, customers, and other entities. Built with **FastAPI** for the backend and **HTML, CSS, JavaScript** for the frontend.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Project](#running-the-project)
- [API Endpoints](#api-endpoints)
- [Troubleshooting](#troubleshooting)

---

## Project Overview

The ChocHouseProject enables CRUD (Create, Read, Update, Delete) operations for various entities in ChocHouse's inventory and customer management. This includes main categories, subcategories, customers, allergies, and ingredients.

The **frontend** provides a user interface for interacting with the backend, which is implemented using **FastAPI** and communicates with a **SQLite** database.

---

## Technologies Used

- **Backend**: FastAPI, Python, SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **API Documentation**: FastAPI Swagger

---

## Project Structure

```
ChocHouseProject/
├── backend/
│   ├── main.py               # FastAPI application with routes
│   ├── database.py           # Database connection setup (SQLite)
│   ├── models.py             # Optional: ORM models for entities
│   └── requirements.txt      # List of backend dependencies
│
├── frontend/
│   ├── index.html            # Main HTML file for the frontend UI
│   ├── style.css             # CSS for frontend styling
│   ├── script.js             # JavaScript to interact with the API endpoints
│
│
└── README.md                 # Project documentation and setup instructions
```

---

## Setup Instructions

### Prerequisites

- **Python 3.8+**
- **MySQL** database with a database named `chochouse` (create tables as needed based on the backend files)
- **Node.js** (optional, for frontend server)

### Backend Setup

1. **Navigate to the backend folder**:
   ```bash
   cd ChocHouseProject/backend
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Enable CORS in FastAPI (main.py)**:
   To allow the frontend to access the backend, add the following to `main.py`:
   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://127.0.0.1:5500"],  # Adjust based on frontend origin
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

### Frontend Setup

1. **Configure API URL**:
   - In `script.js`, set `apiUrl` to your backend URL:
     ```javascript
     const apiUrl = "http://127.0.0.1:8000";
     ```

---

## Running the Project

### 1. Run the Backend Server

Start the FastAPI backend server with Uvicorn:

```bash
uvicorn main:app --reload
```

The server will run on [http://127.0.0.1:8000](http://127.0.0.1:8000).

### 2. Run the Frontend

You can open the `index.html` file in your browser directly or serve it with a local server.

#### Direct Method
Open `index.html` in your browser by double-clicking it or using:
```bash
# On macOS/Linux
open frontend/index.html

# On Windows
start frontend/index.html
```

#### Optional: Serve Frontend with a Local Server

- **Using Python's Built-In HTTP Server**:
  ```bash
  cd frontend
  python -m http.server 5500
  ```
  This serves files at [http://127.0.0.1:5500](http://127.0.0.1:5500).

- **Using Node.js’s `http-server` (if installed)**:
  ```bash
  npm install -g http-server
  cd frontend
  http-server -p 5500
  ```
  Access the frontend at [http://127.0.0.1:5500](http://127.0.0.1:5500).

---

## API Endpoints

Each endpoint is defined in `main.py` and allows for CRUD operations. Here are some common endpoints:

| Method | Endpoint                  | Description                         |
|--------|----------------------------|-------------------------------------|
| `GET`  | `/maincategory`            | Get all main categories             |
| `POST` | `/maincategory`            | Add a new main category             |
| `PUT`  | `/maincategory?id={id}`    | Update a main category by ID        |
| `DELETE` | `/maincategory?id={id}`  | Delete a main category by ID        |

Additional routes are available for subcategories, customers, allergies, and ingredients. Refer to the FastAPI Swagger docs:

- **Interactive API Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Troubleshooting

- **CORS Errors**: If your frontend cannot communicate with the backend due to CORS issues, ensure you’ve correctly added the `CORSMiddleware` in `main.py` with `allow_origins` set to the frontend’s address (`http://127.0.0.1:5500`).

- **Database Errors**: If you encounter errors related to database connection:
  - Confirm your MySQL server is running.
  - Double-check your credentials and database name in `database.py`.
  - Ensure tables are created in the `chochouse` database.

- **Frontend Not Displaying Data**: If data doesn’t display after loading, make sure:
  - The `apiUrl` in `script.js` matches the backend URL (`http://127.0.0.1:8000`).
  - The backend server is running and accessible.

---

## Docker Containerisation

- Open the Command Palette and run the Dev Containers: Add Dev Container Configuration Files
- Select Python 3
- Select SQLite as an additional feature to be installed, press OK, and then select Keep Defaults.
- Open the devcontainer.json file.
- Make necessary changes

