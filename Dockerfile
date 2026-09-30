FROM python:3.12-slim

WORKDIR /app

COPY Taller8.py .

CMD ["python", "Taller8.py"]