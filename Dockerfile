FROM python:3.11-slim

# Install Tkinter and dependencies
RUN apt-get update && apt-get install -y python3-tk

# Install dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the Python app into the container
WORKDIR /app
COPY app.py /app/

# Set the command to run the Python script
CMD ["python3", "app.py"]
