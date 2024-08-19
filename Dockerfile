FROM python:3.10-slim
RUN pip install --upgrade pip
WORKDIR /app/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src .
CMD ["python3", "main.py"]
