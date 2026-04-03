# AuthAPI — Authentication & AI Inference Service
🚀 **Live demo:** https://auth-service-5ilo.onrender.com/docs
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
```

### Run the server

```bash
uvicorn app.main:app --reload
```

The API will be live at `http://localhost:8000`

Interactive docs available at `http://localhost:8000/docs`

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

### Run a prediction

```bash
curl -X POST http://localhost:8000/ai/predict \
  -H "Authorization: Bearer <your_token>" \
  -H "Content-Type: application/json" \
  -d '{"input": "your input data here"}'
```

---

## Project structure

```
app/
├── main.py                  # App entry point
├── api/
│   ├── auth/
│   │   └── router.py        # Register, login, /me routes
│   └── ai/
│       ├── router.py        # Predict, metadata routes
│       └── service.py       # Model inference logic
└── core/
    ├── security.py          # JWT creation and verification
    └── dependencies.py      # Route dependencies (get_current_user)
requirements.txt
README.md
```

---

## Swagger UI

Once the server is running, open `http://localhost:8000/docs` in your browser to get an interactive API explorer where you can test every endpoint without writing any code.

To test protected routes in Swagger:
1. Call `/auth/login` and copy the token from the response
2. Click **Authorize** at the top right
3. Paste your token as `Bearer <token>`
4. All protected routes are now unlocked

---

## Running tests

```bash
pytest tests/
```

---

## Why I built this

Most auth tutorials hand you a library and tell you to call `.login()`. I wanted to understand what's actually happening — token signing, password hashing, route protection, model serving — so I built it myself.

This project is part of my journey from self-taught developer to backend + AI engineer. Follow along on https://www.linkedin.com/in/abolaji-oyinloye-764ab0133

---

## Roadmap

- [ ] Deploy to Railway / Render
- [ ] Add refresh token support
- [ ] Add rate limiting
- [ ] Expand AI model support
- [ ] Add Docker support

---

## Author

Built by **Abolaji Habeeb Oyinloye** — backend & AI engineer.

https://www.linkedin.com/in/abolaji-oyinloye-764ab0133/ · [GitHub](https://github.com/Abolajioyin) ·
