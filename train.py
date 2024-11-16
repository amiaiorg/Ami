import os
import zipfile
import torch
import pandas as pd
from model import Model
from data_sources.archetypes import ArchetypeBlender
from data_sources.user_neural_pattern import UserNeuralPattern
from data_processing.process_data import DataProcessingLayer

def main():
    print("Welcome to AMI Training")

    # Download and extract the dataset
    os.system('kaggle datasets download -d openhermes/openhermes -p ./data')
    with zipfile.ZipFile('./data/openhermes.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')

    # Load the dataset
    dataset_path = './data/openhermes.csv'  # Adjust the path based on the extracted files
    data = pd.read_csv(dataset_path)

    # Initialize the model
    input_dim = data.shape[1] - 1  # Assuming the last column is the target
    output_dim = 1  # Adjust based on your target
    model = Model(input_dim, output_dim, context="professional")

    # Initialize the data processing layer
    data_processing_layer = DataProcessingLayer(model)

    # Process the data and train the model
    data_processing_layer.process_data('my_bucket', 'my_object')

    # Save the trained model
    model.save_model('trained_model.pth')
    print("Model training complete and saved as 'trained_model.pth'")

if __name__ == "__main__":
    main()