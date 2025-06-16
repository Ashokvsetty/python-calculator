# GitHub Actions CI/CD Setup Guide

## Overview

This repository includes comprehensive GitHub Actions workflows for:

- 🔨 **Automated Docker builds** and pushes to Docker Hub
- 🧪 **Automated testing** across multiple Python versions
- 🔍 **Security scanning** with Trivy and Hadolint
- 📦 **Multi-platform builds** (AMD64 + ARM64)
- 🏷️ **Smart tagging** based on branches and releases

## Quick Setup

### Step 1: Configure Docker Hub Secrets

You need to add Docker Hub credentials to your GitHub repository secrets:

1. **Go to your repository on GitHub**
2. **Click Settings → Secrets and variables → Actions**
3. **Add these repository secrets:**

   | Secret Name | Value | Description |
   |-------------|-------|-------------|
   | `DOCKER_HUB_USERNAME` | `ashokvsetty` | Your Docker Hub username |
   | `DOCKER_HUB_ACCESS_TOKEN` | `your-token-here` | Docker Hub access token |

### Step 2: Create Docker Hub Access Token

1. **Log in to Docker Hub**: https://hub.docker.com/
2. **Go to Account Settings → Security → Access Tokens**
3. **Create New Access Token**:
   - Name: `GitHub Actions Calculator`
   - Permissions: `Read & Write`
4. **Copy the token** and add it as `DOCKER_HUB_ACCESS_TOKEN` secret

### Step 3: Enable GitHub Actions

GitHub Actions should be enabled by default, but verify:
1. **Go to your repository → Actions tab**
2. **If prompted, click "I understand my workflows, go ahead and enable them"**

## Workflows Explanation

### 1. Docker Build & Push (`docker-build-push.yml`)

**Triggers:**
- 📤 Push to `main` or `develop` branches
- 🏷️ New version tags (`v*`)
- 🔄 Pull requests to `main`
- 🔄 Manual dispatch with custom tags

**Features:**
- 🌍 Multi-platform builds (AMD64 + ARM64)
- 💿 Build caching for faster builds
- 🧪 Automated testing of built images
- 🏷️ Smart tagging strategy
- 📋 Release notes generation

**Generated Tags:**
```bash
# On main branch push:
ashokvsetty/docker-repo:calculator
ashokvsetty/docker-repo:latest
ashokvsetty/docker-repo:main-<sha>

# On version tag (e.g., v1.0.0):
ashokvsetty/docker-repo:calculator
ashokvsetty/docker-repo:latest
ashokvsetty/docker-repo:1.0.0
ashokvsetty/docker-repo:1.0
ashokvsetty/docker-repo:1

# On develop branch:
ashokvsetty/docker-repo:develop
ashokvsetty/docker-repo:develop-<sha>
```

### 2. Security Scanning (`security-scan.yml`)

**Triggers:**
- 📤 Push to `main` or `develop`
- 🔄 Pull requests to `main`
- ⏰ Daily at 2 AM UTC
- 🔄 Manual dispatch

**Features:**
- 🔍 Trivy vulnerability scanning
- 🔍 Docker image security analysis
- 🛡️ Dockerfile linting with Hadolint
- 📋 Security reports in GitHub Security tab

### 3. Testing (`test.yml`)

**Triggers:**
- 📤 Push to `main` or `develop`
- 🔄 Pull requests to `main`
- 🔄 Manual dispatch

**Features:**
- 🐍 Multi-Python version testing (3.9-3.12)
- 🔍 Code linting with flake8
- 🧪 Application startup testing
- 🐳 Docker container testing
- 🌐 HTTP endpoint validation

## Usage Scenarios

### Scenario 1: Regular Development

```bash
# Make changes to your code
git add .
git commit -m "Add new feature"
git push origin main
```

**What happens:**
1. ✅ Tests run on multiple Python versions
2. ✅ Security scans execute
3. ✅ Docker image builds and pushes to Docker Hub
4. ✅ Image gets tagged as `calculator` and `latest`

### Scenario 2: Creating a Release

```bash
# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0
```

**What happens:**
1. ✅ All tests and security scans run
2. ✅ Docker image builds with semantic version tags
3. ✅ Release notes are generated
4. ✅ Multiple image tags created: `v1.0.0`, `1.0.0`, `1.0`, `1`, `latest`

### Scenario 3: Manual Deployment

1. **Go to Actions tab in GitHub**
2. **Select "Build and Push Docker Image"**
3. **Click "Run workflow"**
4. **Enter custom tag (optional)**
5. **Click "Run workflow"**

### Scenario 4: Pull Request Testing

```bash
# Create feature branch
git checkout -b feature/new-calculator-button
# Make changes and push
git push origin feature/new-calculator-button
# Create PR on GitHub
```

**What happens:**
1. ✅ Tests run automatically
2. ✅ Security scans execute
3. ✅ Docker builds (but doesn't push)
4. ✅ All checks must pass before merge

## Monitoring and Troubleshooting

### View Workflow Status

1. **Repository → Actions tab**
2. **Click on any workflow run**
3. **View logs and results**

### Common Issues

#### 1. Docker Hub Authentication Failed
```
Error: denied: authentication failed
```
**Solution:**
- Check `DOCKER_HUB_USERNAME` secret
- Regenerate `DOCKER_HUB_ACCESS_TOKEN`
- Ensure Docker Hub repository exists

#### 2. Tests Failing
```
Pytest or flake8 errors
```
**Solution:**
- Check code syntax
- Fix linting issues
- Ensure Python compatibility

#### 3. Security Scan Failures
```
Trivy found vulnerabilities
```
**Solution:**
- Update base Docker image
- Check Dockerfile best practices
- Review security recommendations

#### 4. Build Cache Issues
```
Slow builds or cache errors
```
**Solution:**
- Manually clear cache in Actions
- Check Dockerfile layer optimization

### View Results

- **Docker Hub**: https://hub.docker.com/r/ashokvsetty/docker-repo
- **Security Reports**: Repository → Security → Code scanning alerts
- **Build Logs**: Repository → Actions → Workflow runs

## Advanced Configuration

### Custom Docker Repository

To change the Docker Hub repository:

1. **Edit `.github/workflows/docker-build-push.yml`**
2. **Change `DOCKER_HUB_REPO` environment variable**
3. **Update secrets accordingly**

### Additional Platforms

To add more build platforms:

```yaml
# In docker-build-push.yml
platforms: linux/amd64,linux/arm64,linux/arm/v7
```

### Custom Triggers

To add more trigger conditions:

```yaml
on:
  push:
    branches: [ main, develop, staging ]
    paths: 
      - 'src/**'
      - 'Dockerfile'
```

## Security Best Practices

- 🔐 **Never commit secrets** to repository
- 🏢 **Use repository secrets** for sensitive data
- 🔄 **Rotate access tokens** regularly
- 🔍 **Monitor security alerts** in GitHub Security tab
- 📋 **Review workflow permissions** regularly

## Next Steps

After setup:

1. ✅ **Make a test commit** to trigger workflows
2. ✅ **Verify Docker images** appear on Docker Hub
3. ✅ **Check security reports** in GitHub
4. ✅ **Create your first release** with version tag
5. ✅ **Set up branch protection** rules if needed

## Support

If you encounter issues:

1. **Check workflow logs** in Actions tab
2. **Review this documentation**
3. **Check GitHub Actions documentation**
4. **Verify Docker Hub permissions**

