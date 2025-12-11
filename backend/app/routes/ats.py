# app/routes/ats.py

from fastapi import APIRouter, UploadFile, File, Form
from app.services.resume_parser import parse_resume
from app.services.scraper import scrape_job_description
from app.services.cleaners.jd_cleaner import clean_and_extract_jd
from app.services.cleaners.resume_cleaner import clean_and_score_resume
from app.services.resume_parser import parse_resume

router = APIRouter()


@router.post("/analyze")
async def analyze_resume(
    file: UploadFile = File(...),
    job_url: str = Form(None),
    pasted_text: str = Form(None)
):
    # Step 1: Read and parse resume
    content = await file.read()
    parsed_resume = parse_resume(file.filename, content)

    # Step 2: Get raw job description
    # Step 2: Get raw job description
    if job_url and (job_url.startswith("http://") or job_url.startswith("https://")):
        raw_jd = scrape_job_description(job_url)
    elif job_url:
        # If job_url is provided but not a valid URL, treat it as pasted text
        raw_jd = job_url
    elif pasted_text:
        raw_jd = pasted_text
    else:
        return {"error": "Please provide a job URL or paste the job description."}

    # Step 3: Clean job description
    jd_data = clean_and_extract_jd(raw_jd)

    results = parse_resume(file.filename, content)

    result = clean_and_score_resume(parsed_resume["text"], jd_data)
    return {
        "job_description": jd_data,
        "resume_analysis": result,
        "resume_text": results["text"][:3000],
        "detected_title": results["detected_title"]
    }
