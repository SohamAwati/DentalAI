from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, Any

from app.schemas import ScanResult, InsightsResponse
from app.services.pipeline import (
    check_quality,
    detect_and_classify,
    calculate_severity,
    determine_archetype,
    get_insights
)

app = FastAPI(title="DentalAI Backend API")

# Allow CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"status": "ok", "message": "DentalAI Backend is running."}

@app.post("/api/scan", response_model=ScanResult)
async def scan_image(file: UploadFile = File(...)):
    """
    Endpoint to upload a scan, run quality check, detect teeth, classify, and score.
    """
    # Read image
    image_bytes = await file.read()
    
    # 1. Quality Check
    quality_result = check_quality(image_bytes)
    if not quality_result["passed"]:
        return ScanResult(
            quality_passed=False,
            quality_reason=quality_result["reason"],
            teeth=[],
            overall_risk_score=0.0,
            archetype="unknown"
        )
    
    # 2. Detection & Classification
    teeth_data = detect_and_classify(image_bytes)
    
    # 3. Severity Regression
    severity_score = calculate_severity(teeth_data)
    
    # 4. Archetype Lookup (Clustering matching)
    archetype = determine_archetype(severity_score)
    
    return ScanResult(
        quality_passed=True,
        quality_reason=None,
        teeth=teeth_data,
        overall_risk_score=severity_score,
        archetype=archetype
    )

@app.get("/api/insights", response_model=InsightsResponse)
def get_insights_endpoint():
    """
    Returns precomputed clustering + association rule results.
    """
    return get_insights()
