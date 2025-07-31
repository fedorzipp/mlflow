import os
import mlflow
import boto3
import pandas as pd
from io import StringIO
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def read_data_from_s3(bucket_name, key):
    s3 = boto3.client('s3')
    csv_obj = s3.get_object(Bucket=bucket_name, Key=key)
    body = csv_obj['Body'].read().decode('utf-8')
    data = pd.read_csv(StringIO(body))
    return data

def main():
    bucket = os.getenv("S3_BUCKET_NAME")
    key = os.getenv("S3_DATA_KEY")

    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:7001"))
    mlflow.set_experiment("mlops-pipeline-experiment")

    print("Tracking URI:", mlflow.get_tracking_uri())

    print("Loading dataset from S3...")
    df = read_data_from_s3(bucket, key)

    X = df.drop('Survived', axis=1)
    y = df['Survived']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        acc = accuracy_score(y_test, preds)

        mlflow.log_param("max_iter", 200)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")

        print(f"Model accuracy: {acc}")

if __name__ == "__main__":
    main()
