import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from config.config import GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET, GITHUB_CALLBACK_URL

router = APIRouter()

@router.get("/auth/github/login")
def github_login():
    return {
        "login_url" : f"https://github.com/login/oauth/"
    }

