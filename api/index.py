from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
templates = Jinja2Templates(directory="templates")

chat_history = []

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {
        "request": request,
        "chat_history": chat_history
    })

@app.post("/ask", response_class=HTMLResponse)
async def ask_gpt(request: Request, prompt: str = Form(...)):
    try:
        chat_history.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chat_history
        )
        reply = response.choices[0].message.content
        chat_history.append({"role": "assistant", "content": reply})
    except Exception as e:
        chat_history.append({"role": "assistant", "content": f"❌ Error: {str(e)}"})

    return templates.TemplateResponse("form.html", {
        "request": request,
        "chat_history": chat_history
    })

# Vercel requires `app` to be exported
handler = app
