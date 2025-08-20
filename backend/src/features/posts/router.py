from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from infra.database import get_db
from features.posts import service, schema
from features.user import model as user_model

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schema.PostResponse)
def create_post(post: schema.PostCreate, db: Session = Depends(get_db), user_id: int = 1):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return service.create_post(db, post, user_id)


@router.get("/", response_model=list[schema.PostResponse])
def list_posts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return service.list_posts(db, skip, limit)

@router.get("/{post_id}", response_model=schema.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = service.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post
