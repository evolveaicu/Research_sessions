# 📘 AI Personality Chatbot

A simple full-stack AI chatbot that allows users to chat with an AI model whose personality can be customized. The backend uses FastAPI + Groq API, and the frontend is a clean HTML/CSS/JS interface.

## 🚀 Features

- Customizable AI personality
- FastAPI backend with Groq's Llama model
- Fully responsive UI
- Real-time chat messages
- Loading indicator
- CORS-enabled (works locally without issues)

## 📂 Project Structure

```
/project
│── main.py        # FastAPI backend
│── .env           # Groq API key
│── index.html     # Frontend UI
│── README.md
```

## 🔧 Backend Setup (FastAPI + Groq)

### 1. Install Python 3.10+

Check with:

```bash
python --version
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

Create a `requirements.txt` (or use these commands):

```bash
pip install fastapi uvicorn groq python-dotenv
```

### 4. Add your .env file

Inside the project folder, create a `.env` file and add:

```
GROQ_API_KEY=YOUR_KEY_HERE
```

👉 Get your API key from: https://console.groq.com

### 5. Run the backend

Run FastAPI with:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

You should see:

```
Uvicorn running on http://127.0.0.1:8000
```

Your API is now ready at: `POST http://localhost:8000/chat`

## 🎨 Frontend Setup

You already have the `index.html`.

### Open the file

Just double-click `index.html` to open it in your browser.

OR use a local server:

```bash
npx serve
```

## 🔗 Connecting Frontend + Backend

The frontend calls:

```javascript
fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        message: text,
        personality: personality
    })
});
```

Make sure:
- ✔ Backend is running on port 8000
- ✔ You opened the frontend locally (`index.html`)

## 🧪 Testing the API

Use curl:

```bash
curl -X POST http://localhost:8000/chat \
-H "Content-Type: application/json" \
-d '{"message":"Hi","personality":"Friendly AI"}'
```

## 🐞 Common Errors & Fixes

### ❌ CORS error

Enable CORS (already done in your code):

```python
allow_origins=["*"]
```

### ❌ API key missing

Make sure `.env` exists and you restarted the server.

### ❌ 404 not found

Run from correct directory:

```bash
uvicorn main:app --reload
```

## 🎉 You're Ready!

1. Open `index.html`
2. Run backend: `uvicorn main:app --reload`
3. Start chatting with your AI bot! 🚀