from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import DATABASE_URL

# SQLAlchemy 엔진 생성
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 하면 SQL 실행 로그 출력 (개발용)

# 세션 팩토리 생성 (DB 연결 관리)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# SQLAlchemy 모델을 위한 Base 클래스
Base = declarative_base()

# DB 세션을 반환하는 함수 (FastAPI 의존성 주입에 사용)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
