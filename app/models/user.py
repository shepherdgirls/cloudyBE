from sqlalchemy import Column, int, String
from config.config import Base

class User(Base):
    __tablename__ = "users" # 테이블명

    user_id = Column(int, primary_key = True, index = True)
    github_username = Column(String, unique = True, nullable = False)