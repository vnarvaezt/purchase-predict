![pylint](https://img.shields.io/badge/PyLint%20Score-7.18-orange?logo=python&logoColor=white)
# purchase-predict 
## Overview

This repository contains a Kedro project generated using `Kedro 0.19.5`. The project aims to test Kedro as a framework for managing machine learning workflows, and it integrates with MLflow for experiment tracking and Flask for serving models via an API.

## **Installation**

### **Prerequisites**

* Python 3.9+
* Docker (for containerization)
* Kedro
* MLflow

## Running the project with Docker

https://github.com/user-attachments/assets/245e1a2d-309a-47cb-be27-19503fa8561d

1. **Clone the repositories** :

```python
git clone https://github.com/vnarvaezt/purchase-predict.git
git clone https://github.com/vnarvaezt/purchase-predict_api.git
```

2. Set up docker for each project

```
cd purchase-predict-api
docker compose up -d --build
cd purchase-predict
docker compose up -d --build
```

# Running the project locally

https://www.youtube.com/watch?v=vUMTCgx-8hg

1. **Clone the repository** :

```bash
git clone https://github.com/vnarvaezt/purchase-predict.git
cd purchase-predict
```

2. Install requirements

```bash
pip install -r requirements.txt
```

3. Set up docker
   ```bash
   docker build -t kedro_mlflow_app .
   ```
4. Configure environment variables :

* For MLflow, set up the following variables in `.env` or your environment:

```bash
export MLFLOW_SERVER=http://localhost:5000
export EXPERIMENT_NAME=purchase-predict
export ENV="local"
```

5. Start mlflow server locally

   ```bash
   mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./mlflow_artifacts --host 0.0.0.0

   ```
6. Running the project

   ```bash
   kedro run
   ```
