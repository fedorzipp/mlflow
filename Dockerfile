FROM python:3.10-slim

RUN pip install --no-cache-dir mlflow scikit-learn boto3 pandas

WORKDIR /app
COPY train.py /app/
COPY upload_dataset.py /app/
