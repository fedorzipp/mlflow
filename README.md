# MLOps Pipeline with Docker Compose and AWS S3

Цей проєкт демонструє базовий MLOps pipeline з використанням:

- AWS S3 для зберігання датасету
- MLflow для логування експериментів
- Docker Compose для запуску MLflow UI, тренування і завантаження датасету

## Запуск

1. Створи S3 bucket в AWS
2. Створи файл .env або експортуй змінні:
   ```
   export AWS_ACCESS_KEY_ID=...
   export AWS_SECRET_ACCESS_KEY=...
   export AWS_DEFAULT_REGION=...
   export S3_BUCKET_NAME=...
   ```
3. Запусти:
   ```
   docker compose up --build
   ```
4. Відкрий MLflow UI: http://localhost:5000
