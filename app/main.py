from fastapi import FastAPI
from app.routers import user, audit
from app.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["User"])
app.include_router(audit.router, prefix="/audit", tags=["Audit"])

