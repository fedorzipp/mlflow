import os
import boto3

def upload_file_to_s3(local_file, bucket_name, s3_key):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket_name, s3_key)
        print(f"Uploaded {local_file} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file: {e}")

def main():
    bucket = os.getenv("S3_BUCKET_NAME")
    local_path = "/data/train.csv"
    s3_key = "train.csv"
    upload_file_to_s3(local_path, bucket, s3_key)

if __name__ == "__main__":
    main()
