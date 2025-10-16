# DevOps Practice Project

This is a minimal web application for practicing CI/CD workflows with Jenkins, SonarQube, Docker, and ArgoCD GitOps deployment to Kubernetes.

## Project Structure

- `app/` - Application source code (REST API)
- `ci/` - Jenkins pipeline and CI/CD scripts
- `docker/` - Dockerfile for local/CI builds
- `k8s/` - Kubernetes manifests and ArgoCD app definitions
- `configs/` - Environment-specific configs (dev, staging, prod)
- `.github/` - Copilot and GitHub-related files

## CI/CD Workflow

- Jenkins pipeline: build, test, SonarQube analysis, Docker build, artifact generation
- SonarQube: code quality checks
- Docker: containerization
- ArgoCD: GitOps deployment to Kubernetes (dev, staging, prod)
- Automated promotion between environments

## Getting Started

1. Clone the repository
2. Review the Jenkinsfile and pipeline scripts in `ci/`
3. Build and run the app locally with Docker
4. Deploy to Kubernetes using ArgoCD manifests in `k8s/`

---

## Running Locally

To run the application on your local machine using Docker:

```sh
docker build -t devops-practice-app -f docker/Dockerfile .
docker run --rm -p 8000:8000 devops-practice-app
```


---

### Running Locally with Python (No Docker)

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```sh
pip install -r app/requirements.txt
```

3. Start the app:

```sh
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The app will be available at http://localhost:8000

To stop the app, press `Ctrl+C` in the terminal running the server.

This project is designed for hands-on DevOps practice and can be extended for more complex scenarios.
