PySheet-Lite – No-Code Backend Engine for Google Sheets

A lightweight, no-code backend engine that reads data from Google Sheets and classifies text using simple AI logic — all in Python.

---

## Overview

PySheet-Lite is a minimal backend engine designed for developers and non-developers who want to turn Google Sheets into an API instantly. It uses Python + FastAPI for the backend, supports dynamic sheet reading, and comes with built-in text classification using keyword-based logic — making it easy to deploy, test, and extend.

---

##  Features

- ✅ Read data from Google Sheets via `gspread`
- ✅ Text classification without any external AI models (`keyword-based`)
- ✅ Modular structure with clean Python code (`models/`, `services/`, `templates/`)
- ✅ UI interface with HTML + JS (no React.js / no frontend frameworks)
- ✅ Open-source & ready to extend with real AI models later
- ✅ Public deployment ready (Render.com / Railway.app)

---

##  Installation

Clone repository:
  bash
git clone https://github.com/username/pysheet-lite.git 
cd pysheet-lite




Install dependencies: 
pip install fastapi uvicorn gspread oauth2client



 How to Run: 
 uvicorn main:app --reload


  Endpoints: GET /data/{sheet_name} : Returns JSON data from a Google Sheet. : GET http://localhost:8000/data/sample-sheet
→ { "sheet": "sample-sheet", "data": [...] }



  
