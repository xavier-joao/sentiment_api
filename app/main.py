from app.services.sentiment import classify_sentiment
from app.api import routes
from fastapi import FastAPI
from app.api.schemas import ReviewInput  
from app.db.database import engine, Base

app = FastAPI(title="Sentiment Analysis API")
app.include_router(routes.router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Sentiment API is up and running"}