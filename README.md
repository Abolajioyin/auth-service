## 🚀 Production-Ready AI Inference API

This project is a secure, scalable AI inference backend built with FastAPI.

It demonstrates real-world AI engineering practices:
- JWT Authentication & protected routes
- Model inference served through REST APIs
- Clean modular backend architecture
- Production-style project structure

Goal: showcase AI engineering skills through deployable backend systems — not notebooks.


---
  
## 🏗 Architecture

Client (Swagger/Postman/Frontend)
|
| 1) POST /auth/register
| 2) POST /auth/login
v
+-------------------+
| Auth Router |
+-------------------+
|
| hash/verify password (bcrypt)
| create token (JWT)
v
+-------------------+
| Security Layer |
| bcrypt + JWT |
+-------------------+
|
| returns: access_token
v
Client stores token
|
| 3) POST /ai/predict
| Authorization: Bearer <token>
v
+-------------------+
| AI Router |
+-------------------+
|
| Depends(get_current_user)
v
+-------------------+
| Dependencies |
| decode/verify JWT |
+-------------------+
| |
| OK | Fail
v v
+-------------------+ 401 Unauthorized
| Inference Service |---------------------> Client
| model pipeline |
+-------------------+
|
v
Prediction response -> Client

## ✅ Features

### Authentication
- `POST /auth/register` — create a user
- `POST /auth/login` — login and receive an access token (JWT)
- `GET /auth/me` — protected route to verify token + user identity

## 🧠 Why This Project Matters

Most AI projects stop at training models.

This project focuses on:
- Serving models through APIs
- Authentication & security
- Production-ready backend structure

This mirrors how real AI systems are deployed in industry.


### AI Inference
- `POST /ai/predict` — protected endpoint for model inference  
  *(currently supports a baseline inference implementation; upgrade path includes real model artifacts + versioning)*

---

## 🛠 Tech Stack

- Python
- FastAPI
- JWT Authentication
- Pydantic
- Uvicorn
- HuggingFace Transformers (AI inference)


---

## 📁 Project Structure

```text
app/
  main.py
  api/
    auth/
      router.py
    ai/
      router.py
      service.py
  core/
    security.py
    dependencies.py
requirements.txt
README.md

## 📌 Author

**Abolaji Habeeb Oyinloye**
AI Engineer in Progress 🚀
Building production-ready AI systems.

