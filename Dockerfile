# Select the base image that is best for our application
FROM python:3

# Install any operating system junk


# Set the working directory to copy stuff to
WORKDIR /app

# Copy all the code you want to copy from the local directory into the image (can use COPY . . to do all or specifiy which ones by name)
COPY accounts accounts
COPY attendees attendees
COPY common common
COPY conference_go conference_go
COPY events events
COPY presentations presentations
COPY requirements.txt requirements.txt
COPY manage.py manage.py

# Install any language dependencies
RUN pip install -r requirements.txt

# Set the command to run the application
CMD gunicorn --bind 0.0.0.0:8000 conference-go.wsgi