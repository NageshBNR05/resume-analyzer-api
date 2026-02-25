from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.routes.resume_routes import router as resume_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(resume_router)

@app.get("/")
def home():
    return {"message": "Resume Analyzer API Running"}