#!/bin/bash
set -e

until pg_isready -h db -p 5432 -U "$POSTGRES_USER"; do
  echo "Waiting for postgres..."
  sleep 2
done

REVIEW_COUNT=$(PGPASSWORD="$POSTGRES_PASSWORD" psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -t -c "SELECT count(*) FROM information_schema.tables WHERE table_name = 'review';" | xargs)

if [ "$REVIEW_COUNT" = "0" ]; then
  echo "Seeding database..."
  python seed.py
else
  echo "Database already seeded."
fi

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload