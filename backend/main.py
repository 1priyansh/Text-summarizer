from fastapi import FastAPI
from backend.routers import auth, notes
from backend.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Notes Summarizer API")

app.include_router(auth.router)
app.include_router(notes.router)
