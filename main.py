from fastapi import FastAPI
from models.google_sheet import fetch_data
from services.ai_analyzer import SheetAnalyzer

app = FastAPI()
analyzer = SheetAnalyzer()

@app.get("/data/{sheet_name}")
def get_sheet_data(sheet_name: str):
    try:
        data = fetch_data(sheet_name)
        return {"sheet": sheet_name, "data": data}
    except ValueError as ve:
        return {"error": str(ve)}

@app.get("/analyze")
def analyze_text(text: str):
    result = analyzer.classify(text)
    return result