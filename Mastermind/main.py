from fastapi import FastAPI, Depends, HTTPException
from . import models, crud, database
from .database import engine, Base, SessionLocal
from sqlalchemy.orm import Session

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/interact", response_model=models.UserInteraction)
async def create_interaction(interaction: models.InteractionBase, db: Session = Depends(get_db)):
    return crud.create_interaction(db=db, interaction=interaction)


@app.get("/interact/{interaction_id}", response_model=models.UserInteraction)
async def read_interaction(interaction_id: int, db: Session = Depends(get_db)):
    db_interaction = crud.get_interaction(db, interaction_id=interaction_id)
    if db_interaction is None:
        raise HTTPException(status_code=404, detail="Interaction not found")
    return db_interaction

# Add other routes here as needed
