FROM python:3.9-slim

# Bonnes pratiques Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Créer l'utilisateur non-root
RUN addgroup --system app && adduser --system --ingroup app app

WORKDIR /app

# Dépendances (en root)
COPY --chown=root:root --chmod=644 requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r /app/requirements.txt

# Code applicatif : possédé par root et non inscriptible par l'utilisateur
# 755 = root: rwx ; groupe/autres: r-x (pas d'écriture)
COPY --chown=root:root --chmod=755 main.py /app/main.py

# (Optionnel) Répertoire **écrivable** par l'utilisateur pour logs/tmp
RUN mkdir -p /app/var && chown app:app /app/var
ENV APP_DATA_DIR=/app/var

EXPOSE 5000

# Exécuter en non-root
USER app

CMD ["python", "/app/main.py"]
