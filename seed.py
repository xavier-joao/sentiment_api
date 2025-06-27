import csv
from uuid import uuid4
from datetime import datetime
from app.db.database import SessionLocal
from app.models.review import Review
from app.services.sentiment import classify_sentiment

def seed_from_csv(file_path: str):
    db = SessionLocal()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row["avaliacao"]
            result = classify_sentiment(text)

            review = Review(
                id=uuid4(),
                customer_name=row["nome_cliente"],
                review_date=datetime.strptime(row["data_avaliacao"], "%Y-%m-%d").date(),
                text=text,
                sentiment=result["sentiment"],
                confidence=str(result["confidence"])
            )

            db.add(review)

        db.commit()
        print("✅ Database seeded successfully.")
    db.close()

if __name__ == "__main__":
    seed_from_csv("data/reviews.csv")