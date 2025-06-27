# Sentiment Analysis API / API de Análise de Sentimentos

### **English**  
Analyze customer feedback in real-time using AI (FastAPI + PostgreSQL + [HuggingFace](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)).

## 🚀 Quick Start

```sh
git clone <repo> && cd sentiment_api
docker-compose up
```

## 🔌 Endpoints & cURL Examples

- `POST /reviews` - Analyze text  
  ```sh
  curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"customer_name":"Jane Doe","review_date":"2024-06-27","text":"Great service!"}'
  ```
- `GET /reviews` - List all reviews  
  ```sh
  curl -X GET "http://localhost:8000/reviews"
  ```
- `GET /reviews/{id}` - Get review by ID  
  ```sh
  curl -X GET "http://localhost:8000/reviews/<REVIEW_ID>"
  ```
- `GET /reviews/report?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` - Sentiment report  
  ```sh
  curl -X GET "http://localhost:8000/reviews/report?start_date=2024-01-01&end_date=2025-01-01"
  ```

Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### **Português**  
Analise feedback de clientes em tempo real com IA (FastAPI + PostgreSQL + [HuggingFace](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)).

## 🚀 Início Rápido

```sh
git clone <repo> && cd sentiment_api
docker-compose up
```

## 🔌 Endpoints & Exemplos cURL

- `POST /reviews` - Analisar texto  
  ```sh
  curl -X POST "http://localhost:8000/reviews" -H "Content-Type: application/json" -d '{"customer_name":"João","review_date":"2024-06-27","text":"Ótimo atendimento!"}'
  ```
- `GET /reviews` - Listar todas as avaliações  
  ```sh
  curl -X GET "http://localhost:8000/reviews"
  ```
- `GET /reviews/{id}` - Buscar avaliação por ID  
  ```sh
  curl -X GET "http://localhost:8000/reviews/<REVIEW_ID>"
  ```
- `GET /reviews/report?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` - Relatório de sentimentos  
  ```sh
  curl -X GET "http://localhost:8000/reviews/report?start_date=2024-01-01&end_date=2025-01-01"
  ```

Docs: [http://localhost:8000/docs](http://localhost:8000/docs)
