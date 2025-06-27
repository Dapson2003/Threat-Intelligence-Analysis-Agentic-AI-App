# Use an official Python runtime as a parent image (Python 3.13.5 in this case)
FROM python:3.13.5-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache for faster builds
COPY requirements.txt /app/requirements.txt

# Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application files into the container
COPY . /app

# Expose the port that Streamlit will use
EXPOSE 9002

# Set environment variable to ensure Python output is unbuffered
ENV PYTHONUNBUFFERED=1

# Run app on port 9002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9002"]