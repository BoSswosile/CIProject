#!/bin/bash

# Build and run the complete application locally
echo "🚀 Building CICD Project Docker Images..."

# Build frontend
echo "📦 Building Frontend..."
cd frontend
docker build -t cicd-frontend:latest .
cd ..

# Build backend
echo "📦 Building Backend..."
cd backend
docker build -t cicd-backend:latest .
cd ..

# Build and start with docker-compose
echo "🔧 Starting services with Docker Compose..."
docker-compose up -d

echo "✅ Application is running!"
echo "Frontend: http://localhost:3000"
echo "Backend API: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "To stop the application: docker-compose down"
echo "To view logs: docker-compose logs -f"
