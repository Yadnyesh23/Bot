# Use an official Python runtime as base image
FROM python:3.13

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app.py"]


