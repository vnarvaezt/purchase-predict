FROM python:3.9-slim
RUN apt update \ 
&& apt install -y --no-install-recommends \
&& pip install --upgrade pip
RUN mkdir MODEL
WORKDIR /MODEL
COPY requirements.txt /MODEL/
COPY purchase_predict/src /MODEL/
