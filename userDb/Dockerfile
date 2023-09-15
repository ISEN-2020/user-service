# Utiliser l'image PostgreSQL officielle
FROM postgres:latest

# Définir les variables d'environnement pour PostgreSQL
ENV POSTGRES_USER admin
ENV POSTGRES_PASSWORD admin
ENV POSTGRES_DB user

# Déclarer le volume de données
VOLUME /var/lib/postgresql/data

# Copier les scripts SQL initiaux si nécessaire
# COPY init.sql /docker-entrypoint-initdb.d/

# Exposer le port 5432
EXPOSE 5432
