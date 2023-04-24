FROM quay.io/unstructured-io/unstructured:latest

WORKDIR /

COPY main.py ./
COPY requirements.txt ./
COPY server/ ./server/

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "-u", "main.py"]
