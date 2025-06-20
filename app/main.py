from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routes import auth, resumes, users

app = FastAPI(title="Resume Analyzer API")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Register routers
app.include_router(auth.router)
app.include_router(resumes.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to Resume Analyzer API"}
