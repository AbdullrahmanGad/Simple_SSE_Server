FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (if you have one) or install dependencies directly
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY SSE.py .

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "SSE.py"]
