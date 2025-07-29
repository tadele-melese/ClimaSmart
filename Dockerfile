# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY pyproject.toml .
COPY requirements.txt .
RUN pip install --upgrade pip && pip install .

# Copy the source code
COPY . .

# Default command (can be overridden)
CMD ["climasmart", "--help"]
