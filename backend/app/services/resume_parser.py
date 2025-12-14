import fitz
import re
import pytesseract
from io import BytesIO
from PIL import Image
from collections import Counter
from docx import Document
import docx2txt

def parse_resume(filename, content):
    text = ""
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(content)
    elif filename.lower().endswith((".jpeg",".jpg",".png")):
        text = extract_text_from_image(BytesIO(content))
    elif filename.endswith(".txt"):
        text = content.decode("utf-8")
    elif filename.endswith(".docx"): 
        text = extract_text_from_docx(BytesIO(content))
    elif filename.endswith(".docx"):
        with open("/tmp/temp_resume.docx", "wb") as f:
            f.write(content)
        text = docx2txt.process("/tmp/temp_resume.docx")
    elif filename.endswith(".txt"):
        text = content.decode("utf-8")

    else:
        return{"error": "Unsupported file format"}
    
    job_title = extract_job_title(text)
    return {
        "text": text,
        "detected_title": job_title
    }

def extract_text_from_pdf(content):
    doc = fitz.open(stream=content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_image(file_like):
    image = Image.open(file_like)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_docx(file_like):
    doc = Document(file_like)
    return "\n".join([p.text for p in doc.paragraphs])

def extract_job_title(text):
    lines = text.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    
    keywords = [
        "developer", "engineer", "analyst", "manager", "consultant", 
        "designer", "administrator", "scientist", "technician", "architect"
    ]
    for line in lines[:10]:  # scan top 10 lines
        for word in keywords:
            if word in line.lower():
                return line
    return None

def extract_keywords(text):
    # Naive keyword extraction
    text = text.lower()
    words = re.findall(r'\b[a-z]{3,}\b', text)
    return Counter(words)

def score_resume_match(resume_keywords, job_description):
    jd_words = re.findall(r'\b[a-z]{3,}\b', job_description.lower())
    jd_counter = Counter(jd_words)

    matched = sum((resume_keywords & jd_counter).values())
    total = sum(jd_counter.values())
    score = round((matched / total) * 100, 2) if total > 0 else 0

    tips = []
    for word in jd_counter:
        if word not in resume_keywords:
            tips.append(f"Missing keyword: {word}")

    return {
        "score": score,
        "matched_keywords": list((resume_keywords & jd_counter).elements()),
        "tips": tips[:10]
    }
