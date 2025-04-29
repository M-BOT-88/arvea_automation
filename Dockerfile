FROM python:3.12-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . /app

# Définir la commande par défaut
CMD ["pytest", "tests/test_passage_commande.py"]
