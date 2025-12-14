# app/services/jd_cleaner.py

import re
from app.services.nlp_matcher import NLPMatcher

matcher = NLPMatcher("")

def clean_and_extract_jd(text: str):
    # Remove LinkedIn/Indeed noise
    trash_patterns = [
        r"Referrals increase.*?",
        r"Get notified about.*?",
        r"Mark.*?",
        r"Seniority level.*?",
        r"Employment type.*?",
        r"Job function.*?",
        r"Industries.*?",
        r"About.*?Company.*?",
    ]
    for pattern in trash_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    # Normalize whitespace and lowercase
    text = re.sub(r"\s+", " ", text).lower()

    # Extract key sections (e.g., Responsibilities, Skills)
    section_matches = re.findall(
        r"(responsibilities|skills|requirements|qualifications|key responsibilities)[\s:]*([\s\S]{0,400})",
        text,
        re.IGNORECASE
    )

    sections = []
    combined_text = ""
    for title, content in section_matches:
        cleaned = re.sub(r"[^a-zA-Z0-9,. ()\n\-]", "", content).strip()
        if len(cleaned) > 20:
            sections.append(f"{title.capitalize()}:\n{cleaned}")
            combined_text += " " + cleaned

    # Use NLP matcher to extract structured data
    matched = matcher.match_text(combined_text)

    return {
        "cleaned_jd": "\n\n".join(sections) if sections else text,
        "skills": matched["it_skills"],
        "soft_skills": matched["soft_skills"],
        "qualifications_required": matched["education"] or ["Not specified"],
        "experience_required": matched["experience"] or ["Not specified"]
    }
