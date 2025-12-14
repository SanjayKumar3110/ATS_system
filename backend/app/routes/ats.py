# app/routes/ats.py

from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.resume_parser import parse_resume
from app.services.scraper import scrape_job_description
from app.services.cleaners.jd_cleaner import clean_and_extract_jd
from app.services.cleaners.resume_cleaner import clean_and_score_resume
from app.services.summary import analyze_resume

router = APIRouter()


@router.post("/analyze")
async def analyze_resume_endpoint(
    file: UploadFile = File(...),
    job_url: str = Form(None),
    pasted_text: str = Form(None)
):
    # Step 1: Read and parse resume
    try:
        file_bytes = await file.read()
        parsed_resume = parse_resume(file.filename, file_bytes)
        resume_text = parsed_resume.get("text", "")

        await file.seek(0)

    except Exception as e:
        raise HTTPException(status_code=400, detail =f"Error reading resume: {str(e)}")

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
    jd_text_for_ai = jd_data.get("description", raw_jd) if isinstance(jd_data, dict) else str(jd_data)
    result = clean_and_score_resume(parsed_resume["text"], jd_data)
    ai_review = analyze_resume(resume_text, jd_text_for_ai, "review")

    return {
        "job_description": jd_data,
        "resume_analysis": result,
        "resume_text": parsed_resume["text"][:3000],
        "detected_title": parsed_resume["detected_title"],
        "ai_analysis": {
            "detailed_review": ai_review
        }
    }
