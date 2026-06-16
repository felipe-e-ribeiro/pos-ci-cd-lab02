FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt ; useradd
COPY src/ /app
USER app
CMD ["python", "calculadora.py"]