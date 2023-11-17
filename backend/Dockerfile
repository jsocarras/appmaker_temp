FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /new_proj

# Install system dependencies required for psutil
# Update the package lists and install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    # Clean up the apt cache to reduce image size
    && rm -rf /var/lib/apt/lists/*

COPY . .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 9000

# Set the entry point for the container
CMD ["python", "fire.py"]