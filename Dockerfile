# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /Users/munasar/minikube-development/K8s-project

# Copy the script into the container
COPY ramadan_script.py .

# Run the script when the container starts
CMD ["python", "ramadan_script.py"]

