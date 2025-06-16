#!/bin/bash

# Docker Hub repository details
DOCKER_HUB_REPO="ashokvsetty/docker-repo"
IMAGE_TAG="calculator"
VERSION="latest"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🐳 Docker Build and Push Script for Calculator App${NC}"
echo -e "${BLUE}=================================================${NC}"
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo -e "${RED}❌ Docker is not installed or not in PATH${NC}"
    echo -e "${YELLOW}Please install Docker Desktop from: https://www.docker.com/products/docker-desktop${NC}"
    exit 1
fi

# Check if Docker is running
if ! docker info &> /dev/null; then
    echo -e "${RED}❌ Docker is not running${NC}"
    echo -e "${YELLOW}Please start Docker Desktop and try again${NC}"
    exit 1
fi

echo -e "${GREEN}✅ Docker is installed and running${NC}"
echo ""

# Build the Docker image
echo -e "${BLUE}🔨 Building Docker image...${NC}"
echo "docker build -t ${DOCKER_HUB_REPO}:${IMAGE_TAG} -t ${DOCKER_HUB_REPO}:${VERSION} ."
echo ""

if docker build -t "${DOCKER_HUB_REPO}:${IMAGE_TAG}" -t "${DOCKER_HUB_REPO}:${VERSION}" .; then
    echo -e "${GREEN}✅ Docker image built successfully${NC}"
else
    echo -e "${RED}❌ Failed to build Docker image${NC}"
    exit 1
fi

echo ""

# Show built images
echo -e "${BLUE}📋 Built images:${NC}"
docker images "${DOCKER_HUB_REPO}"
echo ""

# Login to Docker Hub
echo -e "${BLUE}🔐 Logging in to Docker Hub...${NC}"
echo "Please enter your Docker Hub credentials:"

if docker login; then
    echo -e "${GREEN}✅ Successfully logged in to Docker Hub${NC}"
else
    echo -e "${RED}❌ Failed to login to Docker Hub${NC}"
    exit 1
fi

echo ""

# Push the images
echo -e "${BLUE}📤 Pushing images to Docker Hub...${NC}"

echo "Pushing ${DOCKER_HUB_REPO}:${IMAGE_TAG}..."
if docker push "${DOCKER_HUB_REPO}:${IMAGE_TAG}"; then
    echo -e "${GREEN}✅ Successfully pushed ${DOCKER_HUB_REPO}:${IMAGE_TAG}${NC}"
else
    echo -e "${RED}❌ Failed to push ${DOCKER_HUB_REPO}:${IMAGE_TAG}${NC}"
    exit 1
fi

echo "Pushing ${DOCKER_HUB_REPO}:${VERSION}..."
if docker push "${DOCKER_HUB_REPO}:${VERSION}"; then
    echo -e "${GREEN}✅ Successfully pushed ${DOCKER_HUB_REPO}:${VERSION}${NC}"
else
    echo -e "${RED}❌ Failed to push ${DOCKER_HUB_REPO}:${VERSION}${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}🎉 SUCCESS! Your calculator image has been pushed to Docker Hub${NC}"
echo ""
echo -e "${BLUE}📍 Your images are now available at:${NC}"
echo "   • ${DOCKER_HUB_REPO}:${IMAGE_TAG}"
echo "   • ${DOCKER_HUB_REPO}:${VERSION}"
echo ""
echo -e "${BLUE}🚀 To run your calculator anywhere:${NC}"
echo "   docker run -p 8000:8000 ${DOCKER_HUB_REPO}:${IMAGE_TAG}"
echo ""
echo -e "${BLUE}🌐 Then open: http://localhost:8000${NC}"
echo ""

