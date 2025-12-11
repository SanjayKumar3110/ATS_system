#  AI-Powered ATS & Resume Assistant

An advanced **Applicant Tracking System (ATS)** and **Resume Assistant** built with **FastAPI** (Python) and **React**. This tool helps users optimize their resumes for specific job descriptions using AI-driven scoring and provides personalized improvements via a fine-tuned LLM (Gemma-2b-it).

---

##  Features

### 🔹 Phase 1: ATS Matcher
- **Resume Parsing**: Extracts text from PDF, DOCX, and images.
- **Job Description Analysis**: Scrapes or processes job descriptions (JD).
- **Smart Scoring**: Calculates a match score (0-100%) based on keyword overlap and semantic similarity.
- **Missing Keywords**: Identifies critical skills and keywords missing from the resume.

### 🔹 Phase 2: Resume Upgrader & AI Chat
- **Resume Upgrader**:
  - Suggests specific improvements for skills, certifications, and projects.
  - Tailors advice based on a desired role (e.g., "Python Developer").
- **AI Chat Assistant (RAG)**:
  - Interactive chat interface to ask questions about the resume.
  - Powered by a **fine-tuned Gemma-2b-it** model with LoRA adapters.
  - Context-aware answers based on the user's resume.

---

##  Tech Stack

### **Backend**
- **Framework**: FastAPI
- **AI/ML**: PyTorch, Transformers, PEFT (LoRA), BitsAndBytes
- **Model**: Google Gemma-2b-it (Fine-tuned)
- **OCR/Parsing**: PyMuPDF (fitz), Tesseract OCR, python-docx
- **Utilities**: Pandas, RapidFuzz

### **Frontend**
- **Framework**: React.js
- **Styling**: Tailwind CSS
- **State Management**: React Hooks

---

##  Installation & Setup

### 1️⃣ Prerequisites
- Python 3.10+
- Node.js & npm
- NVIDIA GPU (Recommended for local LLM inference) or CPU (slower)
- Tesseract OCR installed on your system

### 2️⃣ Backend Setup
```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Add your Hugging Face Token if needed
echo "HF_TOKEN=your_huggingface_token" > .env
```

### 3️⃣ Frontend Setup
```bash
# Navigate to frontend
cd frontend

# Install dependencies
npm install
```

---

##  Usage

### Start the Backend Server
```bash
cd backend
uvicorn app.main:app --reload
```
*The API will run at `http://127.0.0.1:8000`*

### Start the Frontend Application
```bash
cd frontend
npm run dev
```
*The app will run at `http://localhost:5173` (or similar)*

---

##  API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/ats/analyze` | Upload resume & JD to get a match score. |
| **POST** | `/upgrader/upgrade` | Get improvement tips for a specific role. |
| **POST** | `/rag/ask` | Chat with the AI about the resume. |

---

##  Project Structure

```
Resume_AI/
├── backend/
│   ├── app/
│   │   ├── main.py            # API Entry point
│   │   ├── routes/            # API Routes (ats, upgrader, chat)
│   │   ├── services/          # Business logic & AI models
│   │   └── models/            # Local LLM adapters
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── ...
│   └── ...
└── README.md
```

---

##  Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

##  License
This project is licensed under the MIT License.
