# Use an official Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency list first (layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Default command
ENTRYPOINT ["python", "main.py"]
