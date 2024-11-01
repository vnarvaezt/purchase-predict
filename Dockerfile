FROM python:3.12-slim
# use a kedro image instead
RUN apt update
RUN apt install libgomp1 -y
RUN pip install --upgrade pip
RUN python3 --version
RUN mkdir /model
WORKDIR /model
COPY . /model/
ENV ENV=local
ENV MLFLOW_SERVER=http://mlflow:5000
ENV MLFLOW_REGISTRY_NAME=purchase_predict
#COPY requirements.txt /model/
# COPY src/purchase_predict/ /model/
RUN pip install --no-cache-dir -r requirements.txt
#CMD ["kedro", "run", "--pipeline", "preprocessing"]
