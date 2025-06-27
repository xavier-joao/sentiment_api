import uuid
from sqlalchemy import Column, String, Date, Text
from sqlalchemy.dialects.postgresql import UUID
from app.db.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    customer_name = Column(String(100), nullable=False)
    review_date = Column(Date, nullable=False)
    text = Column(Text, nullable=False)
    sentiment = Column(String(20), nullable=False)
    confidence = Column(String(10), nullable=False)
