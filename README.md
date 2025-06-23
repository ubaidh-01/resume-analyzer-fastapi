# 📄 Resume Analyzer API – FastAPI + AI (DeepSeek via OpenRouter)

A smart resume analysis API built with **FastAPI** that lets users upload their resume (PDF), extracts the content, and sends it to a powerful **DeepSeek AI model** to return:

- ✅ Resume improvement suggestions (per section)
- ✅ ATS (Applicant Tracking System) feedback and keyword enhancement
- ✅ A fully rewritten professional resume

---

## ⚙️ Features

- 🧾 Upload PDF resumes
- 🔐 JWT Auth (Register/Login)
- 📤 Resume upload + CRUD
- 🧠 Deep AI integration (OpenRouter + DeepSeek)
- 📊 JSON analysis of:
  - Strengths & weaknesses per section
  - ATS score and keyword feedback
  - Rewritten resume content
- 📂 Clean modular project structure (FastAPI + SQLAlchemy)

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/resume-analyzer-fastapi.git
cd resume-analyzer-fastapi
````

### 2. Setup environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

Sure! Here's the updated `.env` setup section in your `README.md` with the instructions about the OpenRouter key clarified and formatted cleanly:

---

### 3. Add `.env` file

Create a `.env` file in the project root and add the following:

```
SECRET_KEY=your_jwt_secret              # Any random secret key for JWT (e.g., use secrets.token_hex())
OPENAI_API_KEY=your_openrouter_api_key # Get this from OpenRouter
```

#### 🔑 How to get your OpenRouter API key:

1. Visit 👉 [https://openrouter.ai/models?q=deepseek](https://openrouter.ai/models?q=deepseek)
2. Click the **"API"** tab
3. Generate an **API key**
4. Paste it into your `.env` file as shown above

> ✅ You can get a limited number of requests for free when you sign up.

---


## ▶️ Run the API

```bash
uvicorn app.main:app --reload
```

Go to 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI

---

## 🔐 Auth Routes

* `POST /auth/register` – Register with email & password
* `POST /auth/login` – Login to receive JWT

Use JWT in Swagger's **Authorize** button to access protected endpoints.

---

## 📤 Resume Upload & Improvement Flow

1. `POST /resumes/` with a `.pdf` file (form-data)
2. The API:

   * Extracts text using `pdfplumber`
   * Sends it to **DeepSeek** model on OpenRouter
   * Receives structured JSON with:

     * Section-wise strengths, weaknesses, and suggestions
     * ATS compatibility issues & score
     * Rewritten resume content (human + ATS optimized)

---

## 📦 Stack & Dependencies

```txt
fastapi
uvicorn
sqlalchemy
pdfplumber
passlib[bcrypt]
python-jose
pydantic-settings
openai
```

---

## 📁 Project Structure

```
resume-analyzer-fastapi/
│
├── app/
│   ├── routes/            # API routes
│   ├── models/            # SQLAlchemy models
│   ├── crud/              # DB access logic
│   ├── schemas/           # Pydantic schemas
│   ├── utils/             # Auth + GPT logic
│   ├── config.py          # Settings from .env
│   └── main.py            # FastAPI app entrypoint
│
├── uploads/               # Uploaded PDF resumes
├── requirements.txt
├── .env
└── README.md
```

---

## ✨ Sample Output

```json
{
  "analysis": [
    {
      "section": "Summary",
      "strengths": ["Clear job role"],
      "weaknesses": ["Too generic"],
      "suggestions": ["Add metrics", "Focus on achievements"],
      "ats_compatibility": {
        "score": "6",
        "issues": ["No keywords"],
        "keywords_missing": ["Django", "REST API"]
      }
    }
  ],
  "improved_resume": {
    "content": "Ubaid Ur Rehman\nSoftware Engineer | Django Expert\n...",
    "summary": "Added measurable achievements, cleaned layout",
    "style_used": "Modern",
    "optimization_focus": ["ATS", "Quantifiable results"]
  },
  "additional_recommendations": {
    "target_roles": ["Backend Developer", "Python Engineer"],
    "industry_adaptations": ["Add fintech experience for finance roles"],
    "formatting_tips": ["Use clean headings and consistent spacing"]
  }
}
```

---

## 🧠 Powered by

* [DeepSeek Chat v3 via OpenRouter.ai](https://openrouter.ai)
* FastAPI
* PDFPlumber for text extraction

---

## 👨‍💻 Author

Built by [Ubaid Ur Rehman](https://github.com/ubaidurrehman)
Feel free to fork and improve.

---

## 🪪 License

MIT License – Free to use, modify, and share.


