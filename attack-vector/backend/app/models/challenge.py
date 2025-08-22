from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime, func, UniqueConstraint
from sqlalchemy.orm import relationship
from app.core.db import Base

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, default="")

    challenges = relationship("Challenge", back_populates="category")

class Challenge(Base):
    __tablename__ = "challenges"
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(50), nullable=False)
    points = Column(Integer, nullable=False, default=100)
    flag_hash = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    # Storyline support for OSINT / sequenced challenges
    storyline = Column(String(100), nullable=True)  # e.g., "DarkMarket Heist"
    sequence = Column(Integer, nullable=True)  # order inside storyline

    category = relationship("Category", back_populates="challenges")
    submissions = relationship("Submission", back_populates="challenge", cascade="all, delete-orphan")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    challenge_id = Column(Integer, ForeignKey("challenges.id"), nullable=False)
    flag_submitted = Column(String(255), nullable=False)
    correct = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="submissions")
    challenge = relationship("Challenge", back_populates="submissions")

    __table_args__ = (UniqueConstraint('user_id', 'challenge_id', 'correct', name='unique_correct_per_user_challenge'),)
