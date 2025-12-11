# app/services/nlp_matcher.py

""" It is a nlpmatcher and it is resuable script 
    This script is used in resume_cleaner and jd_cleaner
    It uses dataset file clean_job_data.csv"""

import os
import pandas as pd
import spacy
from rapidfuzz import process, fuzz

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# ---- 1. Load CSV & Build Lookup Sets ---- #

def load_skill_sets_from_csv(csv_path: str):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, '..', 'data', 'csv', 'job_data.csv')
    csv_path = os.path.abspath(csv_path)
    df = pd.read_csv(csv_path).fillna("")

    def clean_column(column):
        terms = set()
        for cell in df[column]:
            for item in str(cell).split(","):
                cleaned = item.strip().lower()
                if cleaned:
                    terms.add(cleaned)
        return terms

    skill_sets = {
        "it_skills": clean_column("IT Skills"),
        "soft_skills": clean_column("Soft Skills"),
        "education": clean_column("Education"),
        "experience": clean_column("Experience"),
    }

    return skill_sets

# ---- 2. NLP Normalization ---- #

def extract_keywords(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop
    ]
    return list(set(tokens))

# ---- 3. Fuzzy Matching ---- #

def fuzzy_match_keywords(tokens, dataset, threshold=85):
    matches = set()
    for token in tokens:
        match, score, _ = process.extractOne(token, dataset, scorer=fuzz.token_sort_ratio)
        if score >= threshold:
            matches.add(match)
    return matches

# ---- 4. Main Matcher ---- #

class NLPMatcher:
    def __init__(self, csv_path: str):
        self.skill_sets = load_skill_sets_from_csv(csv_path)

    def match_text(self, text: str):
        tokens = extract_keywords(text)

        return {
            "it_skills": sorted(fuzzy_match_keywords(tokens, self.skill_sets["it_skills"])),
            "soft_skills": sorted(fuzzy_match_keywords(tokens, self.skill_sets["soft_skills"])),
            "education": sorted(fuzzy_match_keywords(tokens, self.skill_sets["education"])),
            "experience": sorted(fuzzy_match_keywords(tokens, self.skill_sets["experience"])),
        }
