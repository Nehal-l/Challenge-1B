FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for llama-cpp and fitz
RUN apt-get update && apt-get install -y \
    build-essential \
    libopenblas-dev \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
