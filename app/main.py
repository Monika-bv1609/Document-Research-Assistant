from fastapi import FastAPI

from app.database.connection import engine, Base
from app.models.user import User
from app.routes.health import router as health_router
from app.routes.user import router as user_router
from app.routes.ai import router as ai_router


# Creates tables automatically in PostgreSQL.
Base.metadata.create_all(bind=engine)  

app = FastAPI()

app.include_router(health_router)
app.include_router(user_router)
app.include_router(ai_router)

@app.get("/")
async def home():
    return {"message": "AI Research Assistant Running"}