import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# GitHub OAuth 환경 변수 설정
GITHUB_CLIENT_ID = os.getenv("CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
GITHUB_CALLBACK_URL = os.getenv("GITHUB_CALLBACK_URL")

# PostgreSQL 데이터베이스 URL 
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")





