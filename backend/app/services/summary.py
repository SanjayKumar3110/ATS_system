import os
import pypdf
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
current_dir = os.path.dirname(os.path.abspath(__file__))

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
env_path = os.path.join(root_dir, ".env")
load_dotenv(env_path)

api_key = os.getenv("GENAI_API")
if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

genai.configure(api_key=api_key)

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = pypdf.PdfReader(file)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def analyze_resume(resume_input, job_description, analysis_type="review"): 
    prompts = {
        "review": """
            You are an experienced Technical Human Resource Manager. 
            Review the provided resume text against the job description. 
            Share your professional evaluation on whether the candidate's profile aligns with the role. 
            Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
            Evaluate the resume text against the provided job description and list out required missing keywords.
            1. Strengths: [List]
            2. Weaknesses: [List]
            3. Missing keywords: [List]
            4. Final Thoughts: [Summary]
        """
    }

    resume_text = ""
    # Check if input is a file path
    if isinstance(resume_input, str) and len(resume_input) < 256 and os.path.isfile(resume_input):
        resume_text = extract_text_from_pdf(resume_input)
    else:
        resume_text = resume_input

    if not resume_text:
        return "Error: Could not process resume text."
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content([prompts[analysis_type], resume_text, job_description])
        return response.text
    except Exception as e:
        return f"Error connecting to AI Model: {e}"
