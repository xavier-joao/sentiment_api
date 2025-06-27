from pydantic import BaseModel
from datetime import date
from typing import List

class ReviewInput(BaseModel):
    customer_name: str
    review_date: date
    text: str

class ReviewOutput(BaseModel):
    id: str
    customer_name: str
    review_date: date
    sentiment: str
    confidence: float
    text: str  
