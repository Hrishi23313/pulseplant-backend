# PulsePlant Backend Starter

Stack: FastAPI + Uvicorn + SQLAlchemy + Pydantic + SQLite (dev)

This starter includes Member-2A (Machine Health & Analytics) and Member-2B (Shift & Attendance).

Structure:
- database.py
- main.py
- models/
- schemas/
- crud/
- routers/
- utils/

Run locally:
```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

Docs: http://127.0.0.1:8000/docs
