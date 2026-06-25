# Customer Support Agent

## Overview

This project is an AI-powered customer support chatbot built using FastAPI, Streamlit, and Groq LLM.

Features:

* Order tracking
* Return policy information
* FAQ handling
* Hindi to English translation
* Customer escalation for complaints
* AI-generated responses for general queries

## Technologies Used

* Python
* FastAPI
* Streamlit
* LangChain
* Groq API
* Deep Translator
* Docker

## Running the Backend

```bash
uvicorn main:app --reload
```

Backend URL:

http://127.0.0.1:8000

## Running the Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL:

http://localhost:8501

## API Endpoint

POST /chat

Example Request:

```json
{
  "message": "Track order 1001"
}
```

Example Response:

```json
{
  "response": "Order 1001 Status: Shipped"
}
```

## Project Architecture

User → Streamlit → FastAPI → Customer Support Agent → Groq LLM → Response
