FROM python:3.11.15-slim-bookworm

RUN apt-get update -y && apt-get install -y --no-install-recommends awscli \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]