from fastapi import FastAPI
from pydantic import BaseModel

from analyzer.analyzer import analyze_request
from analyzer.models import ProjectAnalysis

app = FastAPI(
    title="Pre-Sales Analyzer",
    description="AI-powered software project pre-sales analysis API",
    version="0.1.0",
)

class AnalysisRequest(BaseModel):
    request: str

@app.post("/analyze", response_model=ProjectAnalysis)
def analyze(request: AnalysisRequest) -> ProjectAnalysis:
    return analyze_request(request.request)