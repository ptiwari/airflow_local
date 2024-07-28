# Apache Airflow with Docker Compose

This README provides a guide to set up and run Apache Airflow using Docker Compose.

## Prerequisites

Before getting started, ensure you have Docker and Docker Compose installed on your system.

## Setup and Run Apache Airflow

1. **Clone the Repository**:

   Clone your Git repository to get the project files:

   ```sh
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Build and Start the Services**:

   Build the Docker image and start the Airflow services using Docker Compose:

   ```sh
   docker-compose up --build
   ```

   This command will build the Docker image specified in your `Dockerfile` and start the Airflow services defined in your `docker-compose.yml` file.

3. **Access the Airflow Web UI**:

   Once the services are up and running, you can access the Airflow web UI by navigating to [http://localhost:8080](http://localhost:8080) in your web browser.

   Use the following credentials to log in:
   - **Username**: `admin`
   - **Password**: `admin`

4. **Managing Airflow DAGs and Plugins**:

   - Place your Airflow DAGs in the `dags/` directory.
   - Place your Airflow plugins in the `plugins/` directory.

   These directories are mounted as volumes in the Docker container, so any changes you make will be reflected in the running Airflow instance.

5. **Stopping the Services**:

   To stop the running Airflow services, press `Ctrl+C` in the terminal where `docker-compose up` is running. To remove the services, run:

   ```sh
   docker-compose down
   ```

## Troubleshooting

- Ensure Docker and Docker Compose are properly installed and running.
- Check the logs for any errors:

  ```sh
  docker-compose logs
  ```

- Verify that the necessary ports (e.g., 8080) are not being used by other services on your machine.

## Conclusion

You now have Apache Airflow running with Docker Compose. You can start developing and scheduling your workflows using Airflow's web interface.

If you have any questions or encounter issues, consult the [Airflow documentation](https://airflow.apache.org/docs/) or reach out to the community for support.
