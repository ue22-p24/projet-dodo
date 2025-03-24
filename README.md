# Le Projet "TODO"

Une Todo-list simple, avec une base de données.

## Description

Ce projet est une réimplémentation du concept de Doodle or Die, développée avec :
- FastAPI pour l'API backend
- SQLite pour la persistance des données
- Templates Jinja2 pour le rendu frontend

## Fonctionnalités

- Lecture et affichage des TODOs en base
- Effacement
- Modification

## Installation

1. Récupérer le code de l'exemple
   ```bash
   npx degit https://github.com/ue12-p24/projet-todo
   ```

2. Installer les dépendances
   ```bash
   uv sync
   ```

3. Créér la base
   ```bash
   uv run db/seed.py
   ```

4. Lancer le serveur:

   - en mode *dev*
     ```bash
     uv run fastapi dev main.py
     ```
   - en mode *prod*
     ```bash
     uv run main.py
     ```

## Lancer les tests

Suivant l 'état d'avancement du cours, on rajoutera des tests dans le répertoire `/tests`

Pour les exécuter:
```bash
uv run pytest
```

## Technologies Utilisées

- Backend : FastAPI
- Base de données : SQLite
- Frontend : HTML/CSS/JavaScript
- Templates : Jinja2

## Contexte Pédagogique

Ce projet est destiné aux élèves de première année de Mines ParisTech dans le cadre de leur formation en développement web. Il sert de support pédagogique pour l'apprentissage des technologies web modernes.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou proposer une pull request.

## Licence

MIT
