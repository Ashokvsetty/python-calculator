# Python Calculator Application

A beautiful web-based calculator application built with Python and containerized with Docker.

## Features

- **Clean Modern UI**: iOS-style calculator interface
- **Full Functionality**: Basic arithmetic operations (+, -, ×, ÷)
- **Additional Functions**: Clear, plus/minus toggle, percentage
- **Keyboard Support**: Use your keyboard for input
- **Responsive Design**: Works on desktop and mobile
- **Containerized**: Easy deployment with Docker

## Quick Start

### Using Docker (Local Build)

1. **Build the container image:**
   ```bash
   docker build -t python-calculator .
   ```

2. **Run the container:**
   ```bash
   docker run -p 8000:8000 python-calculator
   ```

3. **Access the calculator:**
   Open your browser and go to `http://localhost:8000`

### Using Docker Hub (Pre-built Image)

**Quick start - no build required:**
```bash
docker run -p 8000:8000 ashokvsetty/docker-repo:calculator
```
Then open `http://localhost:8000`

**For deployment automation:**
```bash
# Use the automated script
./build-and-push.sh
```

See [DOCKER_GUIDE.md](DOCKER_GUIDE.md) for detailed Docker deployment instructions.

### Using GitHub Actions (Automated CI/CD)

**Automated builds on every commit:**
- ✅ Automatic Docker builds and pushes to Docker Hub
- ✅ Multi-platform support (AMD64 + ARM64)
- ✅ Security scanning and testing
- ✅ Smart tagging based on branches/releases

**Setup required:**
1. Add Docker Hub credentials to GitHub Secrets
2. Push code to trigger automated builds

See [GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md) for complete CI/CD setup instructions.

### Running Locally

1. **Run the Python script:**
   ```bash
   python3 web_calculator.py
   ```

2. **Access the calculator:**
   Open your browser and go to `http://localhost:8000`

## Container Details

- **Base Image**: python:3.11-slim
- **Port**: 8000
- **User**: Non-root user for security
- **Dependencies**: Only Python standard library

## Keyboard Shortcuts

- **Numbers**: 0-9
- **Operations**: +, -, *, /
- **Decimal**: .
- **Equals**: Enter or =
- **Clear**: Escape or C

## Files

- `web_calculator.py` - Main application file
- `calculator.py` - Desktop GUI version (requires tkinter)
- `Dockerfile` - Container build instructions
- `requirements.txt` - Python dependencies (none required)
- `.dockerignore` - Files to exclude from container build

## Architecture

The application uses Python's built-in `http.server` module to serve a single-page web application. The calculator logic is implemented in JavaScript on the frontend, providing a responsive user experience without requiring additional Python web frameworks.

