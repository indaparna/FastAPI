from fastapi import FastAPI
from routes.notes_app_route import router as note_router
from configurations import Base, engine


app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(note_router)
