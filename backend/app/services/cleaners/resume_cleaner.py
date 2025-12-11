# app/services/resume_cleaner.py

""" This script is resume cleaner it is used to extract matched skills and list out missing skills from resume
    It also used to view final score of resume up compare it with job description
    This script uses nlpmatcher script for resume cleaning process"""

import re
from app.services.nlp_matcher import NLPMatcher

DATASET_FILENAME = "clean_job_data.csv"
matcher = NLPMatcher(DATASET_FILENAME)

# --- Resume Cleaner with NLP Matching ---

def clean_and_score_resume(resume_text: str, jd_data: dict):
    resume_text = re.sub(r"\s+", " ", resume_text.lower())

    # Step 1: Extract structured skills using NLP matcher
    matched_resume = matcher.match_text(resume_text)

    # Step 2: Compare with job description
    matched = {
        "it_skills": [s for s in jd_data.get("skills", []) if s in matched_resume["it_skills"]],
        "soft_skills": [s for s in jd_data.get("soft_skills", []) if s in matched_resume["soft_skills"]],
        "education": [e for e in jd_data.get("qualifications_required", []) if e in matched_resume["education"]],
        "experience": [x for x in jd_data.get("experience_required", []) if x in matched_resume["experience"]]
    }

    missing = {
        "it_skills": [s for s in jd_data.get("skills", []) if s not in matched["it_skills"]],
        "soft_skills": [s for s in jd_data.get("soft_skills", []) if s not in matched["soft_skills"]],
        "education": [e for e in jd_data.get("qualifications_required", []) if e not in matched["education"]],
        "experience": [x for x in jd_data.get("experience_required", []) if x not in matched["experience"]]
    }

    # Step 3: Calculate match score
    def calc_score(matched_list, total_list):
        if not total_list:
            return 100.0
        return round((len(matched_list) / len(total_list)) * 100, 2)

    score = {
        "it_skills": calc_score(matched["it_skills"], jd_data.get("skills", [])),
        "soft_skills": calc_score(matched["soft_skills"], jd_data.get("soft_skills", [])),
        "education": calc_score(matched["education"], jd_data.get("qualifications_required", [])),
        "experience": calc_score(matched["experience"], jd_data.get("experience_required", [])),
    }

    total_score = round(sum(score.values()) / 4, 2)

    return {
        "matched": matched,
        "missing": missing,
        "score": score,
        "total_score": total_score
    }
