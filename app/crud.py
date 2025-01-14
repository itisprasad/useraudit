from sqlalchemy.orm import Session
from app.models import User, AuditLog
from app.schemas import UserCreate

def create_user(db: Session, user: UserCreate):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    log = AuditLog(action="CREATE", details=f"User created: {new_user}")
    db.add(log)
    db.commit()

    return new_user

def get_user(db: Session, user_id: int):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user:
        return existing_user

    return None

def get_users(db: Session):
    return db.query(User).all()

def update_user(db: Session, user_id: int, user: UserCreate):
    existing_user = db.query(User).filter(User.id == user_id).first()
    if existing_user:
        existing_user.name = user.name
        existing_user.email = user.email
        db.commit()

        log = AuditLog(action="UPDATE", details=f"User updated: {existing_user}")
        db.add(log)
        db.commit()

        return existing_user
    return None

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()

        log = AuditLog(action="DELETE", details=f"User deleted: {user}")
        db.add(log)
        db.commit()

def get_audit_logs(db: Session):
    return db.query(AuditLog).all()

