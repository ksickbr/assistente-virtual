import json
from random import choice

def carregar_intents(caminho="intents.json"):
    """
    Carrega os dados de intents a partir do arquivo JSON especificado.
    """
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def responder_por_intent(intent_nome: str) -> str:
    """
    Retorna uma resposta baseada no nome da intent fornecida pelo Dialogflow.
    """
    intents = carregar_intents("intents.json")

    #percorre as intents para encontrar a correspondente e retornar uma resposta aleatória entre as disponíveis
    for nome_intent, dados in intents.items():
        if nome_intent == intent_nome:
            respostas = dados.get("respostas", [])
            if respostas:
                return choice(respostas)
            
    return "Desculpe, não entendi sua pergunta."