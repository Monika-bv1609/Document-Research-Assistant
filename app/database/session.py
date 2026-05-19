from app.database.connection import SessionLocal


def get_db():
    db = SessionLocal()


# FastAPI:

# gives DB session
# after request completes
# automatically closes DB

    try:
        yield db

    finally:
        db.close()