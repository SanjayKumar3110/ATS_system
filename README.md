# AI Resume Matcher (ATS System)

A powerful, full-stack Applicant Tracking System (ATS) that leverages **Generative AI (Google Gemini)** and **Natural Language Processing (NLP)** to analyze resumes against job descriptions. It provides detailed match scores, skill breakdowns, and AI-driven professional summaries to help candidates optimize their profiles.

##  Features

-   **Resume Parsing**: Supports PDF, DOCX, TXT, and Image formats (JPG/PNG) using OCR.
-   **Job Description Extraction**:
    -   Extracts text from Job URLs (LinkedIn, Indeed, etc.).
    -   Supports direct text pasting.
-   **AI-Powered Analysis**:
    -   **Google Gemini Integration**: Generates a professional summary, highlights strengths/weaknesses, and provides a detailed review.
    -   **Intelligent Matching**: Uses NLP (spaCy) and Fuzzy Matching (RapidFuzz) to compare skills.
-   **Scoring System**:
    -   Calculates a match score based on IT Skills, Soft Skills, Education, and Experience.
-   **Visual Dashboard**:
    -   Interactive Pie Charts for score breakdown.
    -   Detailed lists of matched and missing skills.
    -   **AI Professional Summary**: A dedicated section for qualitative AI feedback.
-   **User-Friendly Interface**:
    -   Modern, responsive design built with **React** and **Tailwind CSS**.
    -   One-click startup script.

##  Tech Stack

### Backend
-   **Framework**: FastAPI
-   **Language**: Python
-   **AI Model**: Google Gemini (Generative AI)
-   **NLP & ML**: spaCy, RapidFuzz
-   **OCR**: Tesseract (pytesseract), PyMuPDF (fitz)
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
│   │   └── services/       # Business logic (AI, NLP, Cleaners)
│   ├── data/               # Datasets (CSV)
│   ├── .env                # Environment variables
│   └── requirements.txt    # Python dependencies
│
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── components/     # Reusable UI components
│   │   ├── pages/          # Main application pages
│   └── package.json        # Node.js dependencies
│
├── start.bat               # One-click startup script (Windows)
└── README.md               # Project Documentation
```

##  Installation & Setup

### Prerequisites
-   **Python 3.8+**
-   **Node.js & npm**
-   **Google Gemini API Key**: Get one [here](https://makersuite.google.com/app/apikey).
-   **Tesseract OCR**:
    -   *Windows*: [Download Installer](https://github.com/UB-Mannheim/tesseract/wiki) and add to PATH.
    -   *Linux*: `sudo apt-get install tesseract-ocr`
    -   *Mac*: `brew install tesseract`

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ATS_system
```

### 2. Backend Setup
Navigate to the backend directory and install dependencies:
```bash
cd backend
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

**Environment Configuration**:
Create a `.env` file in the `backend/` directory:
```env
GENAI_API=your_gemini_api_key_here
```

### 3. Frontend Setup
Navigate to the frontend directory and install dependencies:
```bash
cd ../frontend
npm install
```

##  Usage

### Option A: One-Click Start (Windows)
Simply double-click the `start.bat` file in the root directory. This will launch both the backend and frontend in separate windows.

### Option B: Manual Start

**Backend**:
```bash
cd backend
uvicorn app.main:app --reload
```

**Frontend**:
```bash
cd frontend
npm start
```

The application will open at `http://localhost:3000`.
To check out this application visit [ATS System](https://ats-system-three.vercel.app).

##  Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
