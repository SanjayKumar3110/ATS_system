# app/services/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_job_description(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Very basic fallback scraper (can be improved for specific sites)
        text_blocks = soup.find_all(["p", "li"])
        text = " ".join(block.get_text(separator=" ") for block in text_blocks)
        return text
    except Exception as e:
        return f"Error: Could not extract job description - {str(e)}"
