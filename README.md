# Projet CI/CD DevOps

Application full-stack avec pipeline CI/CD complet incluant frontend React, backend FastAPI, base de données PostgreSQL et infrastructure Kubernetes sur Azure.

## 🏗️ Architecture

### Frontend
- **Framework** : React 19.1.0
- **Tests** : Jest, React Testing Library, Cypress (E2E)
- **Linting** : ESLint
- **Port** : 3000

### Backend
- **Framework** : FastAPI (Python)
- **Base de données** : PostgreSQL
- **Tests** : pytest avec coverage
- **Linting** : flake8, black, isort
- **Port** : 8000

### Base de données
- **PostgreSQL** 15-alpine
- **Port** : 5432
- **Base** : employeesdb

### Infrastructure
- **Containerisation** : Docker & Docker Compose
- **Orchestration** : Kubernetes (AKS)
- **Cloud** : Azure
- **IaC** : Terraform

## 🚀 Démarrage rapide

### Développement local

#### Frontend
```bash
cd frontend
npm install
npx react-scripts start  # Démarre sur http://localhost:3000
```

#### Backend
```bash
cd backend
pip install -r requirements.txt -r requirements-dev.txt
uvicorn app.main:app --reload  # Démarre sur http://localhost:8000
```

## 🧪 Tests

### Frontend
```bash
cd frontend           # Tests unitaires
npx open cypress   # Tests E2E
```

### Backend
```bash
cd backend
pytest tests/ --cov=app --cov-report=term-missing
```

## 🛠️ Scripts disponibles

### Frontend
- `npm start` : Démarre le serveur de développement
- `npm run build` : Build de production
- `npm test` : Tests unitaires
- `npm run lint` : Vérification du code
- `npm run cypress:open` : Tests E2E interactifs

### Backend
- `npm start` : Démarre le serveur FastAPI
- `npm test` : Tests avec coverage
- `npm run lint` : Vérification du code (flake8, black, isort)
- `npm run lint:fix` : Correction automatique du code

## 📁 Structure du projet

```
├── frontend/           # Application React
│   ├── src/           # Code source
│   ├── cypress/       # Tests E2E
│   └── build/         # Build de production
├── backend/           # API FastAPI
│   ├── app/           # Code source
│   └── tests/         # Tests unitaires
├── infra/             # Infrastructure
│   ├── k8s/           # Manifestes Kubernetes
│   └── terraform/     # Configuration Terraform
│       └── modules/   # Modules Terraform (AKS, PostgreSQL, etc.)
└── docs/              # Documentation
```

## 🔧 Configuration

### Variables d'environnement
- `DB_HOST` : Hôte PostgreSQL (défaut: localhost)
- `DB_NAME` : Nom de la base (défaut: employeesdb)
- `DB_USER` : Utilisateur PostgreSQL (défaut: postgres)
- `DB_PASSWORD` : Mot de passe PostgreSQL (défaut: postgres)

## 🚀 Déploiement

Le projet inclut une infrastructure complète pour le déploiement sur Azure :
- **AKS** : Cluster Kubernetes managé
- **ACR** : Container Registry
- **PostgreSQL** : Base de données managée
- **Terraform** : Provisioning automatisé de l'infrastructure

## 📚 Technologies utilisées

- **Frontend** : React, Cypress, ESLint
- **Backend** : FastAPI, PostgreSQL, pytest
- **DevOps** : Docker, Kubernetes, Terraform
- **Cloud** : Azure (AKS, ACR, PostgreSQL)
- **CI/CD** : Scripts de build automatisés