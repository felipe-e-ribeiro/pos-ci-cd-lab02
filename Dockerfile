FROM python:3.13.14-trixie
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt ; useradd app
COPY src/ /app
USER app
CMD ["python", "calculadora.py"]