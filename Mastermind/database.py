from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    interaction_id = Column(Integer, ForeignKey('interactions.id'))
    timestamp = Column(DateTime, default=datetime.utcnow)

    interaction = relationship('Interaction', back_populates='histories')

# Add your database models here
