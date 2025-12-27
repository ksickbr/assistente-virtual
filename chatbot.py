import json
import unicodedata
from random import choice

 # Normaliza o texto para facilitar a correspondência
def texto_normalizado(texto: str) -> str:
    """
    Normaliza o texto removendo acentos, convertendo para minúsculas e removendo espaços extras.
    """
    texto = unicodedata.normalize('NFKD', texto)
    texto = texto.lower()
    texto = texto.strip()
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto

# Carrega os dados de intents a partir de um arquivo JSON
def carregar_intents(caminho = "intents.json"):
    """
    Carrega os dados de intents a partir de um arquivo JSON
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

# Responde a mensagem do usuário com base nas intents carregadas
def responder_mensagem(texto_usuario):
 
    """
    Recebe uma mensagem do usuário e retorna uma resposta apropriada.
    """
    intents = carregar_intents("intents.json")
    texto_usuario = texto_normalizado(texto_usuario)

    # Coleta as intenções e suas respectivas respostas
    for intent, dados in intents.items():
        exemplos = dados.get("exemplos", [])
        respostas = dados.get("respostas", [])

        # Verifica se o texto do usuário corresponde a algum exemplo e retorna uma resposta aleatória entre as disponíveis
        for exemplo in exemplos:
            exemplo_normalizado = texto_normalizado(exemplo)
            if exemplo_normalizado == texto_usuario:
                return choice(respostas)
            elif texto_usuario in exemplo_normalizado:
                return choice(respostas)
    return "Desculpe, não entendi sua mensagem. Pode reformular?"

#teste da função
if __name__ ==  "__main__":
   mensagem_usuario = input("Você: ")
   resposta = responder_mensagem(mensagem_usuario)
   print("Chatbot: ", resposta)