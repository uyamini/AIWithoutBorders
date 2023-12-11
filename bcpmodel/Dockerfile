# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to the world outside this container
#EXPOSE 80

# Define environment variable
#ENV NAME Predict

# Run predict.py when the container launches
COPY model/mySeResnextModel.hdf5 /app
COPY predict.py /app
CMD ["python3", "predict.py"]

