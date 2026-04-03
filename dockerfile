# FROM python:3.13-slim

# WORKDIR /app

# # Impedir que o Python gere arquivos .pyc e bufferize a saída
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Instalar dependências do sistema
# RUN apt-get update && apt-get install -y --no-install-recommends\
#     gcc \
#     default-libmysqlclient-dev \
#     pkg-config \
#     && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt ./

# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copiar o projeto para o diretorio de trabalho
# COPY . .

# EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]