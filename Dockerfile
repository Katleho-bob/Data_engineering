# Use Python 3.9 image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app.py /app/

# Install the dependencies
RUN pip install flask pytz datetime

# Set the environment variable for the Node ID
ENV NODE_ID=1

# Expose the port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
