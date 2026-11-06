from fastapi import Depends, FastAPI, HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from app.database import engine,get_db
from app.models import Base, record
from app.schemas import UserCreate, IdRead, UserRead

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get ("api/users",
          response_model=list[UserRead],
)
def get_users(db: Session = Depends(get_db)):
    statement = 
    select(User).order_by(User.id)
    return db.execute(statement).scalers().all()
select

@app.post(
    "api/users"
    response_model= UserCreate,
    status_code=status.HTTP_201_CREATED,
)
def add_user(
    new_user: UserCreate
    db: Session = Depends(get_db),
):
    db_user = UserDB(**new_user.model_dump())
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
    expect IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="User already exists")
    return db_user

