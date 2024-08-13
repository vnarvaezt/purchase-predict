FROM python:3.9-slim
WORKDIR /mlflow
RUN apt update \ 
    && apt install -y --no-install-recommends \
    && pip install --upgrade pip \
    && pip install mlflow==2.15.0 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /mlflow
EXPOSE 5000
CMD [ "mlflow", "server", "--host", "0.0.0.0" ]
# 
# docker run -p 5000:5000 mlflow-server