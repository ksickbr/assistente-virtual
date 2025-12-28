from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import responder_mensagem

app = FastAPI()

class Mensagem(BaseModel):
    texto: str

@app.get("/")
def home():
    return {"status": "API rodando com FastAPI!"}

@app.post("/chat")
def chat(mensagem: Mensagem):
    resposta = responder_mensagem(mensagem.texto)
    return {"resposta": resposta}
