from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.schemas import ReviewInput, ReviewOutput
from app.db.database import SessionLocal
from app.models.review import Review
from app.services.sentiment import classify_sentiment
from uuid import uuid4, UUID
from typing import List
from fastapi import Query
from datetime import date

router = APIRouter()

def get_db():
    """
    Dependency that provides a SQLAlchemy database session.
    Yields:
        db (Session): SQLAlchemy session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/reviews", response_model=ReviewOutput)
def create_review(payload: ReviewInput, db: Session = Depends(get_db)):
    """
    Create a new review and classify its sentiment.
    
    Args:
        payload (ReviewInput): Review data including customer name, review date, and text.
        db (Session): Database session (injected).
    
    Returns:
        ReviewOutput: The created review with sentiment and confidence.
    """
    result = classify_sentiment(payload.text)

    review = Review(
        id=uuid4(),
        customer_name=payload.customer_name,
        review_date=payload.review_date,
        text=payload.text,
        sentiment=result["sentiment"],
        confidence=str(result["confidence"])
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    return ReviewOutput(
        id=str(review.id),
        customer_name=review.customer_name,
        review_date=review.review_date,
        sentiment=review.sentiment,
        confidence=float(review.confidence),
        text=review.text
    )

@router.get("/reviews", response_model=List[ReviewOutput])
def get_all_reviews(db: Session = Depends(get_db)):
    """
    Retrieve all reviews from the database.
    
    Args:
        db (Session): Database session (injected).
    
    Returns:
        List[ReviewOutput]: List of all reviews.
    """
    reviews = db.query(Review).all()
    return [
        ReviewOutput(
            id=str(r.id),
            customer_name=r.customer_name,
            review_date=r.review_date,
            sentiment=r.sentiment,
            confidence=float(r.confidence),
            text=r.text
        ) for r in reviews
    ]

@router.get("/reviews/report")
def get_review_report(
    start_date: date = Query(...),
    end_date: date = Query(...),
    db: Session = Depends(get_db)
):
    """
    Generate a report of reviews within a date range, summarizing sentiment counts.
    
    Args:
        start_date (date): Start date for the report (inclusive).
        end_date (date): End date for the report (inclusive).
        db (Session): Database session (injected).
    
    Returns:
        dict: Report with date range, total reviews, and sentiment summary.
    """
    results = db.query(Review).filter(
        Review.review_date.between(start_date, end_date)
    ).all()

    total = len(results)
    counts = {"positive": 0, "neutral": 0, "negative": 0}
    for r in results:
        counts[r.sentiment] += 1

    return {
        "start_date": str(start_date),
        "end_date": str(end_date),
        "total_reviews": total,
        "summary": counts
    }

@router.get("/reviews/{id}", response_model=ReviewOutput)
def get_review_by_id(id: UUID, db: Session = Depends(get_db)):
    """
    Retrieve a review by its unique ID.
    
    Args:
        id (UUID): Unique identifier of the review.
        db (Session): Database session (injected).
    
    Returns:
        ReviewOutput: The review with the specified ID.
    
    Raises:
        HTTPException: If the review is not found.
    """
    review = db.query(Review).filter(Review.id == id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    return ReviewOutput(
        id=str(review.id),
        customer_name=review.customer_name,
        review_date=review.review_date,
        sentiment=review.sentiment,
        confidence=float(review.confidence),
        text=review.text
    )