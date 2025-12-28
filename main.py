from fastapi import FastAPI, Request
from chatbot import responder_por_intent

app = FastAPI()

@app.post("/webhook/dialogflow")
async def dialogflow_webhook(request: Request):
    """
    Endpoint que recebe requisições do Dialogflow e responde com base nas intents detectadas.)
    """
    body = await request.json()

    intent_nome = body["queryResult"]["intent"]["displayName"]
    
    #Obtém resposta baseada na intent
    resposta = responder_por_intent(intent_nome)

    #Retorna resposta no formato esperado pelo Dialogflow
    return {
        "fulfillmentText": resposta
    }