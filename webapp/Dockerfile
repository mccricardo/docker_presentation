# Base Debian image
FROM debian:8.0

# Update repo and install dependencies
RUN apt-get update && apt-get install -y python-pip

# Set working directory
WORKDIR /opt/app/

# Add webapp code
ADD app /opt/app/

# Install app dependencies
RUN pip install -r requirements.txt

# Logs
RUN mkdir -p /var/log/app

# Expose ports
EXPOSE 5000

# Leave container running the app
CMD python server.py && tail -f /var/log/app/app.log
