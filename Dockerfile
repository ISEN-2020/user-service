FROM python:3.9-slim

# Bonnes pratiques Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Créer un utilisateur non-root pour l'exécution
RUN addgroup --system app && adduser --system --ingroup app app

# Répertoire de travail
WORKDIR /app

# Installer les dépendances (en root), puis on droppera les privilèges
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copier uniquement les fichiers nécessaires, en les possédant par l'utilisateur non-root
COPY --chown=app:app main.py .

# Port de l'app (ex: Flask)
EXPOSE 5000

# Exécuter en non-root (conforme Sonar)
USER app

# Commande de démarrage
CMD ["python", "main.py"]
