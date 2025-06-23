# CICD Project - Docker Setup

This project includes Docker configurations for both frontend (React) and backend (FastAPI) applications.

## Prerequisites

- Docker Desktop installed and running
- Docker Compose installed (usually comes with Docker Desktop)

## Quick Start

### Option 1: Using Docker Compose (Recommended)
```bash
# Build and start all services
docker-compose up --build

# Access the applications:
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
# PostgreSQL: localhost:5432
```

### Option 2: Using the Build Script
```bash
# Make sure the script is executable
chmod +x build.sh

# Run the build script
./build.sh
```

### Option 3: Manual Build

#### Frontend
```bash
cd frontend
docker build -t cicd-frontend .
docker run -p 3000:80 cicd-frontend
```

#### Backend
```bash
cd backend
docker build -t cicd-backend .
docker run -p 8000:8000 cicd-backend
```

## Docker Images

### Frontend Image
- **Base**: nginx:alpine (production-ready)  
- **Build**: Multi-stage build (Node.js → Nginx)
- **Port**: 80 (mapped to 3000)
- **Features**: 
  - Optimized React build
  - Nginx reverse proxy
  - Security headers
  - Gzip compression
  - Static file caching

### Backend Image
- **Base**: python:3.9-slim
- **Port**: 8000
- **Features**:
  - FastAPI application
  - PostgreSQL support
  - Health checks
  - Non-root user
  - Optimized for production

## Environment Variables

### Backend
- `DB_HOST`: Database hostname (default: localhost)
- `DB_NAME`: Database name (default: employeesdb)
- `DB_USER`: Database user (default: postgres)
- `DB_PASSWORD`: Database password (default: postgres)

## Available Commands

### Frontend
```bash
npm run docker:build    # Build Docker image
npm run docker:run      # Run Docker container
```

### Backend
```bash
npm run docker:build    # Build Docker image
npm run docker:run      # Run Docker container
```

## Docker Compose Services

- **frontend**: React application (port 3000)
- **backend**: FastAPI application (port 8000)
- **postgres**: PostgreSQL database (port 5432)

## Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# View logs
docker-compose logs -f
```

## Production Deployment

The Docker images are production-ready and can be deployed to any container orchestration platform like:
- Kubernetes
- Docker Swarm
- Azure Container Instances
- AWS ECS
- Google Cloud Run

## CI/CD Integration

The GitHub Actions workflow automatically:
1. Builds both Docker images
2. Tags them with commit SHA and 'latest'
3. Saves images as artifacts
4. Can be extended to push to container registries
