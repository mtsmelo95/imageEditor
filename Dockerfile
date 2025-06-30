# Usa uma imagem Python oficial e otimizada ('slim') como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /code

# Define variáveis de ambiente para otimizar a execução
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copia o arquivo de dependências primeiro para aproveitar o cache
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copia todo o código da API para o diretório de trabalho
COPY . .

# Expõe a porta em que a API vai rodar
EXPOSE 8000

# O comando para iniciar o servidor Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]