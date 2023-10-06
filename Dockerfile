FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local requirements.txt file to the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install falcon
# RUN pip install gunicorn

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 8000 available to the world outside this container
EXPOSE 8000


# Run app.py when the container launches
CMD ["python", "things.py"]
