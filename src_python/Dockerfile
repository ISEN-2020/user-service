# Utiliser une image de base Python 3.8
FROM python:latest

# Définir une variable d'environnement pour garantir que la sortie Python est envoyée
# sans tamponnement directement au terminal.
ENV PYTHONUNBUFFERED=1

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendance et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application
COPY . .

# Exécuter Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
