from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.formation import formation
from app.pydantic.formation import formation as formation_pydantic
from app.pydantic.record_pass import record_pass as record_pass
from app.models.offensive_play_result import offensive_play_result
from app.models.pass_play import pass_play
from app.models.run_play import run_play
from app.pydantic.record_run import record_run
from app.pydantic.pass_play import pass_play as play

offense = APIRouter()


@offense.post("/add_formation")
def add_play(form: formation_pydantic):
    db = SessionLocal()
    db.add(formation(formation_name=form.formation_name))
    db.commit()
    db.close()
    return {"message": "success"}


@offense.post("/add_pass_play")
def add_play(form: play):
    db = SessionLocal()
    # find formation id from formation table
    fmt = (
        db.query(formation)
        .filter(formation.formation_name == form.formation_name)
        .first()
    )
    if not fmt:
        return {"message": "formation not found"}
    db.add(
        pass_play(
            formation_id=fmt.id,
            play_name=form.play_name,
        )
    )
    db.commit()
    db.close()
    return {"message": "success"}


@offense.post("/add_run_play")
def add_play(form: play):
    db = SessionLocal()
    # find formation id from formation table
    fmtn = (
        db.query(formation)
        .filter(formation.formation_name == form.formation_name)
        .first()
    )
    if not formation:
        return {"message": "formation not found"}
    db.add(
        run_play(
            formation_id=fmtn.id,
            play_name=form.play_name,
        )
    )
    db.commit()
    db.close()
    return {"message": "success"}


@offense.post("/record_pass_play")
def add_play(form: record_pass):
    db = SessionLocal()
    # find play id from pass_play table
    formation_id = db.query(formation).filter(formation.formation_name == form.formation_name).first()

    play = db.query(pass_play).filter(pass_play.play_name == form.play_name).filter(pass_play.formation_id == formation_id.id).first()
    if not play:
        return {"message": "play not found"}
    db.add(
        offensive_play_result(
            pass_play_id=play.id,
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


@offense.post("/record_run_play")
def add_run_play(form: record_run):
    db = SessionLocal()
    formation_id = db.query(formation).filter(formation.formation_name == form.formation_name).first()
    # find play id from pass_play table
    #filter by play name and formation id
    play = db.query(run_play).filter(run_play.play_name == form.play_name).filter(run_play.formation_id == formation_id.id).first()
    if not play:
        return {"message": "play not found"}
    db.add(
        offensive_play_result(
            run_play_id=play.id,
            yards=form.yards,
            ball_carrier=form.ball_carrier,
            down=form.down,
            distance=form.distance,
            touchdown=form.touchdown,
            first_down=form.first_down,
            hash=form.hash,
        )
    )
    db.commit()
    db.close()
    return {"message": "success"}


@offense.get("/get_most_successful_play")
def get_most_successful_play() -> play:
    db = SessionLocal()
    # find play id from pass_play table
    ply = (
        db.query(offensive_play_result)
        .filter(offensive_play_result.touchdown == True)
        .first()
    )

    if not ply:
        # get the play with the most yards
        ply = (
            db.query(offensive_play_result)
            .order_by(offensive_play_result.yards.desc())
            .first()
        )
    if ply.pass_play_id:
        ply = db.query(pass_play).filter(pass_play.id == ply.pass_play_id).first()
        fmn = db.query(formation).filter(formation.id == ply.formation_id).first()
    else:
        ply = db.query(run_play).filter(run_play.id == ply.run_play_id).first() 
        fmn = db.query(formation).filter(formation.id == ply.formation_id).first()

    response = play(play_name=ply.play_name, formation_name=fmn.formation_name)
    

    return response
