# AuthAPI — Authentication & AI Inference Service

🚀 **Live demo:** https://auth-service-5ilo.onrender.com/docs
🌐 **Portfolio:** https://portfolio-murex-theta-23.vercel.app

> Note: hosted on Render free tier — first load may take 30-60 seconds to wake up.

A production-ready REST API built with **FastAPI** and **Python** that handles user authentication with JWT tokens and serves AI model predictions through a clean, documented API.

Built from scratch as a demonstration of real backend engineering — not a tutorial clone.

---

## What it does

- **User authentication** — register, log in, and get a secure JWT token back
- **Protected routes** — endpoints that verify your token before responding
- **AI inference** — send data to a live model and get structured predictions
- **Model metadata** — query the model's info, version, and expected inputs
- **Auto-generated docs** — Swagger UI available out of the box

---

## Tech stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.10+ |
| Auth | JWT (JSON Web Tokens) |
| Validation | Pydantic |
| Server | Uvicorn |
| Database | PostgreSQL (Neon) |
| AI | HuggingFace Transformers |
| Docs | Swagger / OpenAPI (auto-generated) |

---

## API endpoints

### Auth

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/register` | Create a new user account |
| `POST` | `/auth/login` | Log in and receive a JWT token |
| `GET` | `/auth/me` | Get the current authenticated user (protected) |

### AI Inference

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/ai/predict` | Submit input and receive a model prediction |
| `GET` | `/ai/metadata` | Retrieve model name, version, and input schema |

---

## Getting started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/Abolajioyin/auth-service.git
cd auth-service

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment variables

Create a `.env` file in the root directory:

```env
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=your-postgresql-connection-string
```

### Run the server

```bash
uvicorn app.main:app --reload
```

Server runs at `http://localhost:8000`
Interactive docs at `http://localhost:8000/docs`

---

## Usage examples

### Register a user

```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

### Log in and get a token

```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Call a protected route

```bash
curl http://localhost:8000/auth/me \
  -H "Authorization: Bearer <your_token>"
```

---

## Project structure

```
app/
├── main.py                  # App entry point
├── models.py                # Database models
├── api/
│   ├── auth/
│   │   └── router.py        # Register, login, /me routes
│   └── ai/
│       ├── router.py        # Predict, metadata routes
│       └── service.py       # Model inference logic
└── core/
    ├── security.py          # JWT creation and verification
    ├── database.py          # PostgreSQL connection
    └── dependencies.py      # Route dependencies
requirements.txt
README.md
```

---

## Live Swagger UI

Test every endpoint without writing any code:
👉 https://auth-service-5ilo.onrender.com/docs

To test protected routes:
1. Call `/auth/login` and copy the token
2. Click **Authorize** at the top right
3. Enter your email and password
4. All protected routes are now unlocked

---

## Running tests

```bash
pytest tests/
```

---

## Why I built this

Most auth tutorials hand you a library and tell you to call `.login()`. I wanted to understand what's actually happening — token signing, password hashing, route protection, model serving — so I built it myself.

---

## Roadmap

- [x] Deploy to Render
- [x] PostgreSQL database integration
- [ ] Add refresh token support
- [ ] Add rate limiting
- [ ] CI/CD with GitHub Actions
- [ ] Docker support

---

## Author

**Abolaji Habeeb Oyinloye** — Backend & AI Engineer

[LinkedIn](https://www.linkedin.com/in/abolaji-oyinloye-764ab0133/) · [GitHub](https://github.com/Abolajioyin) · [Portfolio](https://portfolio-murex-theta-23.vercel.app)
