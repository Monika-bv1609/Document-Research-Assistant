from fastapi import APIRouter

from app.services.ai_service import (
    generate_ai_response
)
from app.schemas.ai_schema import AIRequest

router = APIRouter()


@router.post("/ask-ai")
async def ask_ai(data: AIRequest):

    ai_response = generate_ai_response(
        question=data.question,
        system_prompt=data.system_prompt,
        temperature=data.temperature
    )

    return {
        "question": data.question,
        "system_prompt": data.system_prompt,
        "temperature": data.temperature,
        "ai_response": ai_response
    }