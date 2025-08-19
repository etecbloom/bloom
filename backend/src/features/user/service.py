from sqlalchemy.orm import Session
from . import model, schema
from infra.logger import logger

class UserService:
    def create_user(self, db: Session, user: schema.UserCreate):
        logger.info(f"Criando um usuário com email={user.email}")
        db_user = model.User(
            name=user.name, 
            email=user.email, 
            exp_level=user.exp_level, 
            role=user.role
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        logger.info(f"Usuário criado com id={db_user.id}, role={db_user.role}, exp_level={db_user.exp_level}")
        return db_user


    def get_user(self, db: Session, user_id: int):
        logger.info(f"Buscando usuário id={user_id}")
        return db.query(model.User).filter(model.User.id == user_id).first()
    
    def delete_user(self, db: Session, user_id: int) -> bool:
        user = db.query(model.User).filter(model.User.id == user_id).first()
        if not user:
            return False
        db.delete(user)
        db.commit()

        logger.info(f"Deletado o usuário {user.name}")
        return True