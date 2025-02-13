# Usa a imagem base do Python 3.12
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos de dependências do projeto
COPY pyproject.toml poetry.lock* ./

# Instala as dependências do projeto
RUN poetry install --no-root

# Copia o restante do código da aplicação
COPY . .

# Expõe a porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar a aplicação usando o Poetry
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]