from fastapi import APIRouter, UploadFile, File

from app.utils.resume_ai_feedback import generate_resume_feedback

router = APIRouter()

@router.post("/upload-resume-ai")
async def upload_resume_ai(file: UploadFile = File(...)):

    content = await file.read()
    text = content.decode("utf-8", errors="ignore")

    feedback = generate_resume_feedback(text)

    return {
        "feedback": feedback
    }