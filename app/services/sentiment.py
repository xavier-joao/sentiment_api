import re
import emoji
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

MODEL_NAME = "cardiffnlp/twitter-xlm-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

labels = ['negative', 'neutral', 'positive']

def preprocess(text: str) -> str:
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    text = text.strip()
    return text

def classify_sentiment(text: str) -> dict:
    cleaned = preprocess(text)
    encoded = tokenizer(cleaned, return_tensors='pt', truncation=True)
    with torch.no_grad():
        output = model(**encoded)
    scores = softmax(output.logits.numpy()[0])
    predicted_index = scores.argmax()
    return {
        "sentiment": labels[predicted_index],
        "confidence": round(float(scores[predicted_index]), 4),
        "scores": dict(zip(labels, map(lambda s: round(float(s), 4), scores)))
    }
