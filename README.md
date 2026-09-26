## 🏫 Academic Context
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)

**Student Status:** Computer Science Student  
**Context:** Hands-on training project following a self-directed exploration of backend microservices and digital transformation.  
**Objective:** Building a complete RESTful Web API for national security identity lifecycle management, utilizing Pydantic data modeling, FastAPI routing dependencies, and automated OpenAPI documentation.

---

## 📖 Repository Overview

This repository serves as a practical implementation project for web services architecture, secure state machines, and cyber-security event auditing. It contains a fully functional **FastAPI** backend that simulates a national digital identity checkpoint system, allowing instant identity token deactivation and secure biometric verification cycles.

## 🧠 Key Concepts Explored

### 1. RESTful API Architecture & State Control

* **Verb Mapping:** Implementing explicit HTTP `POST` methods to execute sensitive state modification operations (`/lost`, `/scan`, `/reactivate`).
* **HTTP Response Codes:** Returning explicit standard status codes (`200 OK`, `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`) to accurately communicate token security status to remote client scanners.

### 2. Data Validation & Schemas (Pydantic)

* **Object Modeling:** Mapping critical data relations through the Pydantic `Card` class to ensure structural payload validity.
* **Serialization & Marshalling:** Leveraging `.model_dump()` to effortlessly decouple Pydantic model incoming parameters into system verification logic blocks.

## 🛠️ Technical Summary

| Endpoint / File | Concept Applied | Purpose |
| :--- | :--- | :--- |
| `POST /lost/{card_id}` | `State Modification`, Path Parameters | Simulates a citizen trigger that immediately locks a card status to "Lost". |
| `POST /scan` | `Pydantic Validation`, Data Handling | Simulates bank or checkpoint scanners checking local database status against a payload. |
| `POST /reactivate` | `Biometric Handshake`, Nested Payload | Validates live selfie string tokens to restore a card from "Lost" back to "Active". |
| `app.py` | `FastAPI Core`, Mock Database | Hosts memory-based state dictionaries and aggregates structural routing rules. |
| `security.log` | `Python Logging Framework` | Generated dynamically to trace access logs, system alerts, and security breaches. |

---

