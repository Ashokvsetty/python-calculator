# Docker Deployment Guide

## Prerequisites

1. **Install Docker Desktop**
   - Download from: https://www.docker.com/products/docker-desktop
   - Follow installation instructions for your operating system
   - Start Docker Desktop

2. **Create Docker Hub Account**
   - Sign up at: https://hub.docker.com/
   - Note your username (in this case: `ashokvsetty`)

## Quick Start (Automated)

### Option 1: Use the automated script

```bash
# Make sure you're in the calculator directory
cd calculator

# Run the automated build and push script
./build-and-push.sh
```

The script will:
- ✅ Check if Docker is installed and running
- 🔨 Build the Docker image with proper tags
- 🔐 Login to Docker Hub
- 📤 Push images to your repository
- 📋 Show success message with usage instructions

## Manual Steps (Step by Step)

### Step 1: Build the Docker Image

```bash
# Build with multiple tags
docker build -t ashokvsetty/docker-repo:calculator .
docker build -t ashokvsetty/docker-repo:latest .

# Or build with both tags at once
docker build -t ashokvsetty/docker-repo:calculator -t ashokvsetty/docker-repo:latest .
```

### Step 2: Test the Image Locally

```bash
# Run the container locally to test
docker run -p 8000:8000 ashokvsetty/docker-repo:calculator

# Open browser to http://localhost:8000 to test
# Press Ctrl+C to stop
```

### Step 3: Login to Docker Hub

```bash
docker login
# Enter your Docker Hub username: ashokvsetty
# Enter your Docker Hub password/token
```

### Step 4: Push to Docker Hub

```bash
# Push both tags
docker push ashokvsetty/docker-repo:calculator
docker push ashokvsetty/docker-repo:latest
```

## Verification

### Check Your Images on Docker Hub

1. Visit: https://hub.docker.com/r/ashokvsetty/docker-repo
2. You should see your calculator images listed

### Test Pull and Run from Docker Hub

```bash
# Pull and run from Docker Hub (on any machine with Docker)
docker run -p 8000:8000 ashokvsetty/docker-repo:calculator
```

## Image Details

- **Repository**: `ashokvsetty/docker-repo`
- **Tags**: 
  - `calculator` - Specific tag for the calculator app
  - `latest` - Latest version tag
- **Port**: 8000
- **Base Image**: python:3.11-slim
- **Size**: ~50MB (approximate)

## Usage Examples

### Run with Different Options

```bash
# Basic run
docker run -p 8000:8000 ashokvsetty/docker-repo:calculator

# Run in background (detached)
docker run -d -p 8000:8000 ashokvsetty/docker-repo:calculator

# Run with custom name
docker run -d --name my-calculator -p 8000:8000 ashokvsetty/docker-repo:calculator

# Run on different port
docker run -d -p 9000:8000 ashokvsetty/docker-repo:calculator
# Access at http://localhost:9000
```

### Container Management

```bash
# List running containers
docker ps

# Stop container
docker stop my-calculator

# Remove container
docker rm my-calculator

# View logs
docker logs my-calculator
```

## Troubleshooting

### Common Issues

1. **Docker not running**
   ```
   Error: Cannot connect to the Docker daemon
   ```
   Solution: Start Docker Desktop

2. **Port already in use**
   ```
   Error: Port 8000 is already allocated
   ```
   Solution: Use different port: `-p 8001:8000`

3. **Login failed**
   ```
   Error: authentication failed
   ```
   Solution: Check username/password or use access token

4. **Push permission denied**
   ```
   Error: denied: requested access to the resource is denied
   ```
   Solution: Make sure you're logged in and have access to the repository

### Getting Help

```bash
# Check Docker version
docker --version

# Check Docker info
docker info

# View image details
docker inspect ashokvsetty/docker-repo:calculator
```

## Security Notes

- The container runs as non-root user for security
- Only port 8000 is exposed
- Uses minimal base image (python:3.11-slim)
- No sensitive data is included in the image

## Next Steps

After pushing to Docker Hub, your calculator can be:
- 🚀 Deployed to any cloud platform (AWS, GCP, Azure)
- 🔄 Used in CI/CD pipelines
- 📦 Shared with others easily
- 🌐 Deployed to Kubernetes clusters
- 🏗️ Used in Docker Compose setups

