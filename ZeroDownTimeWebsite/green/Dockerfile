# Base image with Python
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependencies and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY app.py .

# Set environment variables (override via docker-compose)
ENV DEPLOYMENT_COLOR=unset
ENV VERSION_NUMBER=unset
ENV DEPLOYED_AT=unset

# Run the app
CMD ["python", "app.py"]
