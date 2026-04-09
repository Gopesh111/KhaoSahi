# KhaoSahi: Multimodal Food Label Intelligence API

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)]
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?logo=fastapi)]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

KhaoSahi is a privacy-first, API-driven intelligence system designed to analyze consumer food product labels. By combining Multimodal Large Language Models (Vision) with a Medical Retrieval-Augmented Generation (RAG) pipeline, the system detects harmful additives, identifies hidden sugars, and exposes deceptive marketing claims based on established regulatory frameworks (e.g., FSSAI, WHO).

This repository contains the backend architecture, built with a focus on modularity, strict data validation, and fault-tolerant system design.

---

## Core Architecture

The system operates on a multi-stage deterministic and probabilistic pipeline:

1.  **Vision & OCR Ingestion Layer**: Parses uploaded images of product ingredient lists and nutritional tables using vision models.
2.  **Normalization Engine**: Cleans and normalizes noisy OCR data, mapping chemical synonyms (e.g., E319 -> Tertiary butylhydroquinone).
3.  **Medical RAG Pipeline**: Queries a localized FAISS vector database containing chunked regulatory guidelines and medical research to ground the analysis in verifiable science.
4.  **Deterministic Rule Engine**: Performs an O(1) time-complexity pass against known hazardous additives and hidden sugars to establish a baseline risk profile.
5.  **LLM Reasoning Agent**: Synthesizes the baseline rules, RAG context, and raw OCR data to generate a highly structured, explainable JSON response.

---

## Technical Stack

* **Framework**: FastAPI (Asynchronous, High Performance)
* **Data Validation**: Pydantic v2 (Strict Schema Enforcement)
* **Vector Database**: FAISS (Facebook AI Similarity Search)
* **Orchestration**: LangChain (Document chunking and retrieval logic)
* **Inference Engines**: 
    * Vision: Google Gemini 2.5 Flash
    * Reasoning: Groq Llama-3 (70B)

---

## Key Features

* **Deception Scoring**: A proprietary metric that calculates the disparity between front-of-pack marketing claims (e.g., "100% Natural") and back-of-pack realities (e.g., presence of Maltodextrin).
* **Explainable AI**: The system does not just provide a binary "Safe/Unsafe" flag. It returns specific reasons for every flagged ingredient, directly citing regulatory logic.
* **Edge-Case Resiliency**: Engineered to handle blurry images, multilingual text (Hinglish/Hindi/English), and ambiguous marketing jargon gracefully via custom exception handlers.
* **Privacy-First**: No user data or images are permanently stored. Analysis happens in memory, and the context is immediately discarded post-inference.

---

## Project Structure

```text
KhaoSahi-Backend/
├── main.py                     # Application entry point
├── requirements.txt            # Dependency definitions
├── .env.example                # Environment template
├── api/
│   └── v1/
│       ├── endpoints/          # Route handlers (analyze, health)
│       └── router.py           # Main API router
├── core/
│   ├── config.py               # Environment variable management
│   └── exceptions.py           # Custom error handling logic
├── schemas/
│   ├── requests.py             # Input validation schemas
│   └── responses.py            # Strict JSON output schemas
├── services/
│   ├── vision_ocr/             # Image processing and text extraction
│   ├── rag_engine/             # Vector DB and document loaders
│   └── risk_intelligence/      # Deterministic rules and LLM reasoning
└── tests/                      # Pytest suite for API and edge cases

## Installation & Setup

### Prerequisites
* Python 3.9+
* Git

### Local Development

1.  **Clone the repository**
    ```bash
    git clone <paste-your-github-repo-url-here>
    cd KhaoSahi-Backend
    ```

2.  **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure environment variables**
    Copy the example environment file and update it with your API keys.
    ```bash
    cp .env.example .env
    ```

5.  **Run the application**
    ```bash
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
    ```

6.  **Access the Documentation**
    Navigate to localhost:8000/api/docs in your browser to interact with the auto-generated Swagger UI.

---

## API Endpoints

### 1. System Health
* **URL**: /api/v1/health/
* **Method**: GET
* **Description**: Returns the status of the API and underlying microservices (Vector DB, Vision Model, LLM Engine). Useful for load balancer monitoring.

### 2. Analyze Product Label
* **URL**: /api/v1/analyze/
* **Method**: POST
* **Content-Type**: multipart/form-data
* **Description**: Ingests an image of a product label and returns a detailed risk analysis.
* **Parameters**:
    * file (Required): The image file (jpeg, png, webp).
    * product_name (Optional): The name of the product for contextual tagging.

---

## Testing

The project utilizes pytest for unit and integration testing, ensuring robust handling of edge cases (such as low-resolution image uploads).

To run the test suite:
```bash
pytest tests/ -v

---

## Current Status & Roadmap

The current repository demonstrates the comprehensive system architecture, Pydantic data validation pipelines, and deterministic rule engines. Network calls to external LLMs and FAISS indexing are currently configured to run in a mocked environment to demonstrate latency handling, error routing, and schema compliance without incurring API costs.

**Upcoming Milestones:**

- [ ] Integration of live Groq API keys for the reasoning agent.
- [ ] Integration of live Gemini Vision API keys.
- [ ] Population of the FAISS index with the latest FSSAI PDF guidelines.
- [ ] Deployment via Docker containers.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Disclaimer

This system is an AI-based informational tool and does not provide certified medical or legal advice. Information generated should not replace professional dietary consultation.
