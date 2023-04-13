from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.formation import formation

offense = APIRouter()


@offense.post("/add_play")
def add_play():
    db = SessionLocal()
    db.add(formation(formation_name="test"))
    db.commit()
    db.close()
    return {"message": "success"}
