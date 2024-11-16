# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in [requirements.txt](http://_vscodecontentref_/0)
RUN pip install --no-cache-dir -r requirements.txt

# Install additional dependencies (e.g., PyTorch, spaCy)
RUN pip install torch torchvision spacy
RUN python -m spacy download en_core_web_sm

# Make port 80 available to the world outside this container
EXPOSE 80

# Run unit tests
CMD ["pytest"]