- Assistente Virtual com Dialogflow e FastAPI

Projeto de um assistente virtual integrado ao Dialogflow, com backend desenvolvido em FastAPI.

O objetivo do projeto é simular um cenário real de integração entre uma plataforma de IA conversacional e uma API RESTful, aplicando boas práticas de organização, versionamento e arquitetura.



🎯 Objetivos do Projeto

-Criar um assistente virtual que:

-Receba mensagens do usuário via Dialogflow

-Identifique intents utilizando NLP (Dialogflow)

-Retorne respostas por meio de uma API RESTful em FastAPI

-Utilize um arquivo JSON para armazenar respostas associadas às intents

U-tilize Git/GitHub para versionamento e controle de mudanças



🧠 Visão Geral da Arquitetura

-O fluxo de funcionamento do assistente é o seguinte:

-O usuário envia uma mensagem ao assistente.

-O Dialogflow interpreta a mensagem e identifica a intent.

-O Dialogflow envia a intent identificada para a API por meio de um webhook.

-A API, desenvolvida em FastAPI, recebe a requisição.

-A resposta é obtida a partir de um arquivo JSON de intents e respostas.

-A API retorna a resposta ao Dialogflow.

-O Dialogflow exibe a resposta ao usuário final.



🛠️ Tecnologias Utilizadas

-Python 3

-FastAPI — API RESTful

-Dialogflow ES — NLU e gerenciamento de intents

-ngrok — Exposição do webhook local

-JSON — Armazenamento de intents e respostas

-Git / GitHub — Versionamento de código

-Insomnia — Testes de integração da API



📁 Estrutura do Projeto
.
├── main.py          # API FastAPI e endpoint do webhook
├── chatbot.py       # Lógica de resposta baseada em intents
├── intents.json     # Intents e respostas
├── requirements.txt
└── README.md



✅ Funcionalidades Atuais

-Recebimento de mensagens via webhook do Dialogflow

-Identificação de intents por IA (Dialogflow)

-Respostas baseadas em intents definidas em arquivo JSON

-Integração entre Dialogflow e FastAPI

-Testes de integração via Insomnia

-Projeto versionado com Git/GitHub



🚀 Como Executar o Projeto Localmente

1. Criar e ativar o ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

2. Instalar as dependências

pip install -r requirements.txt

3. Executar a API

uvicorn main:app --reload

4. Expor o webhook com ngrok

ngrok http 8000

Copie a URL gerada pelo ngrok e configure no Fulfillment Webhook do Dialogflow.



🧪 Testes

-Os testes principais são realizados diretamente pelo console do Dialogflow

-Também é possível testar a integração simulando requisições via Insomnia

-O endpoint principal é acessado exclusivamente via POST, através do webhook do Dialogflow



🔮 Próximos Passos (Evoluções Futuras)

-Armazenamento de histórico de conversas

-Integração com banco de dados

-Uso de contextos no Dialogflow

-Integração com outras plataformas de IA (ex: Watsonx ou OpenAI)

-Implementação de autenticação e controle de acesso



📄 Licença

Projeto desenvolvido para fins de estudo, aprendizado e demonstração técnica.