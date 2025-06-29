# Use an official Python image as base
FROM python:3.11-slim

# Set a working directory inside the container
WORKDIR /app

# Copy requirements file first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]