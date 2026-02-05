# Authenticated AI Inference Service (FastAPI)

A production-style **AI inference API** built with **FastAPI** that provides:
- **User registration & login**
- **JWT authentication**
- **Protected AI inference endpoint** (`/ai/predict`)
- Clean, scalable project structure designed for real-world ML systems

> Goal: build an AI Engineer–level portfolio by shipping secure, deployable inference services (not notebooks).

---

## ✅ Features

### Authentication
- `POST /auth/register` — create a user
- `POST /auth/login` — login and receive an access token (JWT)
- `GET /auth/me` — protected route to verify token + user identity

### AI Inference
- `POST /ai/predict` — protected endpoint for model inference  
  *(currently supports a baseline inference implementation; upgrade path includes real model artifacts + versioning)*

---

## 🛠 Tech Stack
- Python
- FastAPI
- Uvicorn
- JWT (python-jose)
- Passlib (password hashing)
- python-multipart (OAuth2 form login)
- Git & GitHub

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
