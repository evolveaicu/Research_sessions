from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import uvicorn
from dotenv import load_dotenv
import os

# ---------------------------------------
# 1. CONFIGURE GROQ API
# ---------------------------------------
load_dotenv()  # loads the .env file

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found in .env file!")

client = Groq(api_key=GROQ_API_KEY)
# Choose a Groq model (fast & accurate)
MODEL_NAME = "llama-3.1-8b-instant"  
# others:
# "llama3-70b-8192"
# "mixtral-8x7b-32768"


# ---------------------------------------
# 2. FASTAPI + CORS
# ---------------------------------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------
# 3. REQUEST BODY
# ---------------------------------------
class ChatRequest(BaseModel):
    message: str
    personality: str = "You are a friendly helpful AI assistant."


# ---------------------------------------
# 4. CHAT ENDPOINT
# ---------------------------------------
@app.post("/chat")
async def chat(req: ChatRequest):

    system_prompt = """
    You are Ashok Chitkara and you own Chitkara University.
    You are very proud of your university students and their achievements
    To any user query, respond in such a way that it suggests your love for Chitkara
"""

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": req.message}
            ]
        )

        ai_response = completion.choices[0].message.content

        return {"response": ai_response}

    except Exception as e:
        return {"error": str(e)}


# ---------------------------------------
# 5. RUN SERVER
# ---------------------------------------
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
