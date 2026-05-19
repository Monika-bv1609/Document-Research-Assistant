from pydantic import BaseModel


class AIRequest(BaseModel):

    # Actual user question
    question: str

    # Controls AI behavior/personality
    system_prompt: str = (
        "You are a helpful AI assistant."
    )

    # Controls creativity/randomness
    temperature: float = 0.7