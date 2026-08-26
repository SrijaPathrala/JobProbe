import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "ml"))
from predictor import predict_scam_probability
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from extractor import extract_all
from rules import run_all_rules
from scoring import calculate_risk

app = FastAPI(title="JobProbe API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for hackathon/demo purposes; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---- Request Schema ----
class JobPostingInput(BaseModel):
    text: str  # raw job posting / recruiter message pasted by the user


# ---- Response Schema ----
class AnalysisResult(BaseModel):
    extracted_info: dict
    red_flags: list
    ml_scam_probability: float
    risk_score: int
    risk_level: str
    recommendations: list


@app.get("/")
def read_root():
    return {"status": "JobProbe API is running"}


@app.post("/analyze", response_model=AnalysisResult)
def analyze_job_posting(payload: JobPostingInput):
    text = payload.text

    extracted_info = extract_all(text)
    red_flags = run_all_rules(text, extracted_info)
    ml_scam_probability = predict_scam_probability(text)
    risk = calculate_risk(red_flags, ml_scam_probability)

    recommendations = []
    if risk["level"] in ("Medium", "High"):
        recommendations.append("Verify the company independently through its official website or LinkedIn page.")
        recommendations.append("Never pay any fee to apply for or accept a job offer.")
        recommendations.append("Avoid sharing sensitive personal or financial information before formal verification.")
    elif len(red_flags) > 0:
        recommendations.append("A minor red flag was detected. Proceed with caution and verify recruiter details before responding.")
    else:
        recommendations.append("No red flags detected, but always verify recruiter details before proceeding.")

    return AnalysisResult(
        extracted_info=extracted_info,
        red_flags=red_flags,
        ml_scam_probability=ml_scam_probability,
        risk_score=risk["score"],
        risk_level=risk["level"],
        recommendations=recommendations
    )