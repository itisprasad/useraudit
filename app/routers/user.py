from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserResponse
from app.crud import create_user, get_user, get_users, update_user, delete_user
import traceback

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except Exception as ex:
        traceback.print_exc()
        raise HTTPException(status_code=400, detail="Error creating user details - " + str(ex))

@router.get("/", response_model=list[UserResponse])
def list_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user_data = get_user(db, user_id)  
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data


@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    if delete_user(db, user_id) == True:
        return {"detail": "User deleted"}
    raise HTTPException(status_code=400, detail="User not found")

