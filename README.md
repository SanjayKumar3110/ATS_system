# AI Resume Matcher (ATS System)

A powerful Applicant Tracking System (ATS) tool that uses Natural Language Processing (NLP) to analyze resumes against job descriptions. It provides a detailed match score, skills breakdown, and improvement suggestions.

##  Features

-   **Resume Parsing**: Supports PDF and Image formats (JPG/PNG) using OCR.
-   **Job Description Extraction**:
    -   Extracts text from Job URLs (LinkedIn, Indeed, etc.).
    -   Supports direct text pasting.
-   **Intelligent Matching**:
    -   Uses **spaCy** for NLP tokenization and keyword extraction.
    -   Uses **RapidFuzz** for fuzzy matching against a curated dataset of skills.
-   **Scoring System**:
    -   Calculates a match score based on:
        -   IT Skills
        -   Soft Skills
        -   Education
        -   Experience
-   **Visual Dashboard**:
    -   Interactive Pie Charts for score breakdown.
    -   Detailed lists of matched and missing skills.
-   **User-Friendly Interface**:
    -   Modern, responsive design built with **React** and **Tailwind CSS**.
    -   Loading animations and easy navigation.

##  Tech Stack

### Backend
-   **Framework**: FastAPI
-   **Language**: Python
-   **NLP & ML**: spaCy, RapidFuzz, Transformers (Hugging Face)
-   **OCR**: Tesseract (pytesseract), PyMuPDF
-   **Data Handling**: Pandas

### Frontend
-   **Framework**: React.js
-   **Styling**: Tailwind CSS
-   **Charts**: Recharts
-   **HTTP Client**: Axios

##  Project Structure

```
ATS_system/
├── backend/                # FastAPI Backend
│   ├── app/
│   │   ├── main.py         # Entry point
│   │   ├── routes/         # API endpoints
│   │   └── services/       # Business logic (NLP, Cleaners, Scrapers)
│   ├── data/               # Datasets (CSV)
│   └── requirements.txt    # Python dependencies
│
└── frontend/               # React Frontend
    ├── src/
    │   ├── components/     # Reusable UI components
    │   ├── pages/          # Main application pages
    │   └── api.jsx         # API configuration
    └── package.json        # Node.js dependencies
```

##  Installation & Setup

### Prerequisites
-   **Python 3.8+**
-   **Node.js & npm**
-   **Tesseract OCR**: Required for processing image-based resumes.
    -   *Windows*: [Download Installer](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH.
    -   *Linux*: `sudo apt-get install tesseract-ocr`
    -   *Mac*: `brew install tesseract`

### 1. Backend Setup

Navigate to the backend directory:
```bash
cd backend
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Download the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

Start the Backend Server:
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

### 2. Frontend Setup

Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Start the React Development Server:
```bash
npm start
```
The application will open at `http://localhost:3000`.

##  Usage

1.  Open the web app at `http://localhost:3000`.
2.  **Upload Resume**: Select your resume file (PDF or Image).
3.  **Provide Job Description**:
    -   Paste a link to a job posting (e.g., LinkedIn).
    -   OR paste the full text of the job description.
4.  Click **"Analyze Resume"**.
5.  View your **Match Score**, extracted skills, and suggestions.
6.  Use the **"Analyze New Resume"** button to start over.

##  Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
