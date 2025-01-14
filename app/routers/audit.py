from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_audit_logs
from app.schemas import AuditLogResponse

router = APIRouter()

@router.get("/", response_model=list[AuditLogResponse])
def get_audit_logs_endpoint(db: Session = Depends(get_db)):
    return get_audit_logs(db)

