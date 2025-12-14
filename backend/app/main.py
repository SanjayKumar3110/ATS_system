# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ATS routes
from app.routes import ats

app = FastAPI(
    title="ATS system",
    description=(
        "ATS matcher using NLP• "
    ),
    version="2.1.0"
)

# ────────────────────────────────────────────────────────
# CORS  (frontend access)
# ────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # front-end dev servers, localhost, etc.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ────────────────────────────────────────────────────────
# Include routers            (prefix keeps URLs tidy)
# ────────────────────────────────────────────────────────
app.include_router(ats.router,      prefix="/ats",      tags=["ATS"])

#   POST /ats/analyze

# Run:  uvicorn app.main:app --reload
# Docs: http://127.0.0.1:8000/docs
