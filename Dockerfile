FROM python:3.10-slim
WORKDIR /geobingo
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ..
CMD ["python", "my_package/main.py"]
