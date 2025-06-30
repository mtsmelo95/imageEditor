Removedor de Fundo de Imagens API
Uma API simples e eficiente para remover o fundo de imagens, construída com Python e FastAPI. Ideal para ser integrada em websites, como portfólios, ou para automação de tarefas de edição de imagem.

✨ Recursos Principais
Endpoint único via POST para upload e processamento de imagens.

Utiliza a biblioteca rembg para uma remoção de fundo de alta qualidade, baseada em IA.

Documentação interativa e automática com Swagger UI (/docs).

Pronta para integração com projetos frontend graças à configuração de CORS.

🛠️ Tecnologias Utilizadas
Backend: Python 3.9+

Framework API: FastAPI

Processamento de Imagem: Rembg, Pillow

Servidor ASGI: Uvicorn

🚀 Configuração e Instalação
Siga os passos abaixo para executar o projeto localmente.

1. Clone o repositório

Bash

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2. Crie e ative um ambiente virtual

Bash

# Crie o ambiente virtual

python3 -m venv venv

# Ative o ambiente (macOS/Linux)

source venv/bin/activate

# Ative o ambiente (Windows)

# venv\Scripts\activate

3. Instale as dependências

Bash

pip install -r requirements.txt
⚡ Executando a API
Com o ambiente virtual ativado, inicie o servidor Uvicorn:

Bash

uvicorn main:app --reload
O servidor estará disponível em http://127.0.0.1:8000.

🧪 Como Usar
A maneira mais fácil de testar a API é através da documentação interativa gerada pelo FastAPI.

Abra seu navegador e acesse: http://127.0.0.1:8000/docs.

Localize o endpoint POST /remove-background/ e expanda-o.

Clique no botão "Try it out".

Na seção file, clique em "Choose File" e selecione a imagem que deseja processar.

Clique em "Execute".

A imagem com o fundo removido será exibida na seção de resposta (Response body).
