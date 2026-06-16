FROM python:3.12.13
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt ; useradd app
COPY src/ /app
USER app
CMD ["python", "calculadora.py"]