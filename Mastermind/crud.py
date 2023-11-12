from sqlalchemy.orm import Session
from . import models


def create_interaction(db: Session, interaction: models.InteractionBase) -> models.UserInteraction:
    db_interaction = models.UserInteraction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction


def get_interaction(db: Session, interaction_id: int) -> models.UserInteraction:
    return db.query(models.UserInteraction).filter(models.UserInteraction.id == interaction_id).first()

# Add CRUD operations for other models as needed
