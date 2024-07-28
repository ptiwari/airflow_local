# Use the official Apache Airflow base image
FROM apache/airflow:latest

# Set the working directory to /airflow
WORKDIR /airflow

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install additional Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set the AIRFLOW_HOME environment variable to /airflow
ENV AIRFLOW_HOME=/airflow

# Expose the necessary ports
EXPOSE 8080 5555 8793

USER airflow