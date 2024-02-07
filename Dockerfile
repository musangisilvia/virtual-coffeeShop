# Using an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /vcs
WORKDIR /vcs

# Copy the current directory contents into the container at /vcs
COPY . .
COPY config.py ./flaskr

# Create and activate a virtual environment
# RUN python -m venv venv
# ENV PATH="/app/venv/bin:$PATH"

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"]
