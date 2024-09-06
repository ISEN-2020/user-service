# User-Service

User-Service est un microservice collaboratif qui fonctionne avec les projets Customer UI et Admin UI. Il gère les fonctionnalités d'authentification et de gestion de comptes utilisateur, telles que la création, la connexion et la suppression de comptes.
Table des Matières

    Description
    Installation
    Usage
    Fonctionnalités
    Configuration
    Contribution
    Licence
    Crédits

Description

User-Service est conçu pour répondre aux demandes envoyées depuis les interfaces utilisateur des projets Customer UI et Admin UI. Les actions principales incluent :

    /login : Permet la connexion d'un utilisateur avec vérification des identifiants.
    /register : Permet l'enregistrement d'un nouvel utilisateur.
    /delete : Permet la suppression d'un compte utilisateur.

En fonction de la faisabilité de chaque action (par exemple, la création d'un compte avec une adresse e-mail existante), User-Service renvoie true ou false.
Installation

Pour installer User-Service, suivez les étapes ci-dessous :

    Créez un répertoire vide sur votre machine locale.
    Clonez le projet depuis le dépôt GitHub :

    bash

    git clone https://github.com/ISEN-2020/user-service.git

    Utilisez la pipeline fournie pour lancer le workflow d'installation des dépendances.

Usage

User-Service fonctionne en conjonction avec les projets Customer UI et Admin UI. Pour utiliser ce service :

    Assurez-vous que les projets Customer UI et Admin UI sont correctement configurés et fonctionnent selon leurs instructions (consultez leurs fichiers README respectifs).
    User-Service interagit avec les autres projets via des appels API aux différentes URL disponibles (/login, /register, /delete).

Fonctionnalités

    Login : Authentification des utilisateurs avec vérification des identifiants (retourne true si le login est réussi, sinon false).
    Register : Création de nouveaux comptes utilisateurs (retourne true si l'enregistrement est réussi, sinon false).
    Delete : Suppression des comptes utilisateurs (retourne true si la suppression est réussie, sinon false).

Configuration

Aucune configuration spécifique n'est requise pour User-Service, mais assurez-vous que les projets Customer UI et Admin UI sont correctement configurés pour interagir avec ce service.
Contribution

Les contributions sont les bienvenues ! Pour contribuer :

    Fork le projet.
    Crée une branche avec vos modifications : git checkout -b ma-nouvelle-fonctionnalite.
    Commit vos modifications : git commit -m 'Ajout d'une nouvelle fonctionnalité'.
    Poussez vos modifications : git push origin ma-nouvelle-fonctionnalite.
    Ouvrez une Pull Request.

Crédits

Développé par Aymeric DAUREL, Mathéo BAGNIS et Matthieu GOTTRAU.