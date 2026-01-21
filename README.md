# 🚀 Sentiment Analysis Microservice

![Build Status](https://github.com/YOUR_GITHUB_USERNAME/sentiment-project/actions/workflows/ci_cd.yaml/badge.svg)  
![Python](https://img.shields.io/badge/python-3.9%2B-blue)  
![Docker](https://img.shields.io/badge/container-ready-blueviolet)  
![License](https://img.shields.io/badge/license-MIT-green)

A **cloud-native**, **containerized**, and **production-ready REST API** that performs real-time sentiment analysis on text using NLP.

> This project demonstrates the **complete DevOps lifecycle**—Agile development, CI/CD automation, containerization, observability, and scalable cloud-native design.

---

## 🏗 System Architecture & Workflow

This microservice follows a clean and high-performance workflow:

### 🔄 **End-to-End Processing Flow**

1. **Client Sends Request**  
   A user or external system sends a `POST /analyze` request with raw text.

2. **FastAPI Validates Input**  
   Uses Pydantic models to enforce valid structure.  
   Invalid input → **400 Bad Request**.

3. **Text Sent to NLP Engine (TextBlob)**  
   Computes:
   - **Polarity** (`-1` to `+1`)
   - **Subjectivity** (`0` to `1`)

4. **Sentiment Classification**  
   - Polarity > 0 → **Positive**  
   - Polarity < 0 → **Negative**  
   - Polarity = 0 → **Neutral**

5. **Observability Logging**  
   Each request logs execution time, scores, and error traces for monitoring.

6. **API Returns JSON Response**  
   Includes sentiment label, polarity, and subjectivity.

---
## 🛠 Tech Stack

| Domain | Tool | Version | Purpose in Project |
| :--- | :--- | :--- | :--- |
| **Language** | **Python** | `3.9` | Core application logic and scripting. |
| **Framework** | **FastAPI** | `0.109.0` | High-performance, asynchronous REST API framework. |
| **NLP Engine** | **TextBlob** | `0.17.1` | Sentiment analysis (Polarity & Subjectivity calculation). |
| **Containerization** | **Docker** | `Latest` | Standardizes the environment for Cloud deployment. |
| **CI/CD** | **GitHub Actions** | `v3` | Automates the testing and linting pipelines. |
| **Quality Assurance** | **Flake8** | `7.0.0` | Enforces PEP8 code style and quality. |
| **Testing** | **Pytest** | `8.0.0` | Runs automated unit tests for system validation. |
| **Server** | **Uvicorn** | `0.27.0` | ASGI server implementation to run the FastAPI app. |


