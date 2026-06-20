# Edubase — School Management System

A school management system built using **Python (FastAPI)** for the backend and **HTML/CSS/JS** for the frontend. It has 4 separate logins (portals) for different people in a school — Principal, Staff, Admin, and Parent/Student.

## What it does

Each person who logs in only sees what they need:

- **Principal** — manage teachers, classes, see announcements, approve leave
- **Staff** — mark attendance, enter marks, apply for leave
- **Admin** — handle new student admissions, fees, generate certificates
- **Parent/Student** — check attendance, marks, fees, apply for leave

This is **Phase 1** of the project. In Phase 2, I plan to add Machine Learning on top of this data — like predicting which students might need extra attention based on attendance and marks.

## Tech Used

- Python
- FastAPI (backend framework)
- SQLAlchemy (to talk to the database)
- SQLite (database — just a file, no setup needed)
- JWT (for login/auth, so each user gets a secure token)
- HTML, CSS, JavaScript (frontend)

## Folder Structure

```
edubase/
├── backend/
│   ├── main.py            # Starts the app
│   ├── database.py        # Connects to database
│   ├── models.py          # Database tables
│   ├── auth.py             # Login/token logic
│   ├── schemas.py          # Data formats for requests
│   └── routes/             # API code for each portal
├── frontend/
│   ├── home.html
│   ├── principal/
│   ├── staff/
│   ├── admin/
│   ├── parent_student/
│   └── static/
└── requirements.txt
```

## How to Run

```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload
```

Then open `frontend/home.html` in your browser.

## What's Done So Far

- [x] Folder structure
- [ ] Database tables
- [ ] Login system
- [ ] Backend APIs for all 4 portals
- [ ] Frontend pages
- [ ] Phase 2: ML features