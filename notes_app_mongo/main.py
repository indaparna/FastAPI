from fastapi import FastAPI
from routes.notes_app_route import router as note_router

app = FastAPI()

app.include_router(note_router)
