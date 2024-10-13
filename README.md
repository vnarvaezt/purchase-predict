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

1. **Clone the repositories** :

```python
git clone https://github.com/vnarvaezt/purchase-predict.git
git clone https://github.com/vnarvaezt/purchase-predict_api.git
```

Set up docker for each project


```
cd purchase-predict-api
docker compose up -d --build
cd purchase-predict
docker compose up -d --build
```

# Running the project with Docker

1. **Clone the repository** :

```python
git clone https://github.com/vnarvaezt/purchase-predict.git
cd purchase-predict
```

2. Install requirements

pip install -r requirements.txt

3. Set up docker
   ```bash
   docker build -t kedro_mlflow_app .
   ```
4. **Configure environment variables** :

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
