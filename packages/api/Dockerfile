FROM --platform=linux/amd64 nvidia/cuda:12.2.2-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y software-properties-common && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa && apt-get install -y python3.11 python3-pip

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
