# Set base image (host OS)
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD python ./app.py ${BOT_TOKEN:?no BOT_TOKEN} ${API_URL:?no API_URL}