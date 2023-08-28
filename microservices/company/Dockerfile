# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY compRequirements.txt compRequirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r compRequirements.txt

# Copy the current directory contents into the container
COPY . .

# Specify the command to run your FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
