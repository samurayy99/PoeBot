from pydantic import BaseModel
from typing import Optional
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Pydantic models


class InteractionBase(BaseModel):
    user_id: str
    message: str


class QueryBase(BaseModel):
    user_id: str
    query: str

# Database models


class UserInteraction(Base):
    __tablename__ = 'interactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    message = Column(String)


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    interaction_id = Column(Integer, ForeignKey('interactions.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    interaction = relationship('UserInteraction', back_populates='histories')
