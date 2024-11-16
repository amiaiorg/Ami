# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download the spaCy language model
RUN python -m spacy download en_core_web_sm

# Copy the kaggle.json file to the container
COPY .kaggle/kaggle.json /root/.kaggle/kaggle.json

# Set permissions for the kaggle.json file
RUN chmod 600 /root/.kaggle/kaggle.json

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the training script
CMD ["python", "train.py"]