from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.formation import formation
from app.pydantic.formation import formation as formation_pydantic
from app.pydantic.record_pass import record_pass as record_pass
from app.models.offensive_play_result import offensive_play_result
from app.models.pass_play import pass_play

offense = APIRouter()


@offense.post("/add_formation")
def add_play(form: formation_pydantic):
    db = SessionLocal()
    db.add(formation(formation_name=form.formation_name))
    db.commit()
    db.close()
    return {"message": "success"}


@offense.post("/add_pass_play")
def add_play(form: record_pass):
    db = SessionLocal()
    # find play id from pass_play table
    play = db.query(pass_play).filter(pass_play.play_name == form.play_name).first()
    if not play:
        return {"message": "play not found"}
    db.add(
        offensive_play_result(
            pass_play=play.id,
            caught=form.caught,
            yards=form.yards,
            ball_carrier=form.ball_carrier,
            yac=form.yac,
            down=form.down,
            distance=form.distance,
            touchdown=form.touchdown,
            first_down=form.first_down,
            coverage=form.coverage,
            blitz=form.blitz,
            hash=form.hash,
        )
    )
    db.commit()
    db.close()
    return {"message": "success"}
