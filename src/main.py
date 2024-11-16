from data_sources.user_neural_pattern import UserNeuralPattern
from models.model import Model
from data_sources.archetypes import ArchetypeBlender
import torch
import pandas as pd
import zipfile
import os

def main():
    print("Welcome to AMI")

    # Download and extract the dataset
    os.system('kaggle datasets download -d openhermes/openhermes -p ./data')
    with zipfile.ZipFile('./data/openhermes.zip', 'r') as zip_ref:
        zip_ref.extractall('./data')

    # Load the dataset
    dataset_path = './data/openhermes.csv'  # Adjust the path based on the extracted files
    data = pd.read_csv(dataset_path)

    # Preprocess the dataset
    # Example preprocessing: Select relevant columns and convert to tensor
    input_data = torch.tensor(data[['input_feature1', 'input_feature2']].values, dtype=torch.float32)
    targets = torch.tensor(data[['target_feature']].values, dtype=torch.float32)

    # Example usage of ArchetypeBlender
    blender = ArchetypeBlender()
    context_weights = blender.adjust_for_context("professional")
    personality = blender.blend_personality(context_weights)
    print("Blended Personality:", personality)

    # Example usage of UserNeuralPattern
    user_profile = UserNeuralPattern(user_id="12345")
    user_profile.update_emotional_state("happy")
    user_profile.add_interaction("greeting", "Hello, how can I assist you today?")
    print("User Profile:", user_profile.get_profile())

    # Example usage of Model with DRL and UPN
    input_dim = input_data.shape[1]
    output_dim = targets.shape[1]

    model = Model(input_dim, output_dim, context="professional")

    # Preliminary test: Train DRL model
    print("Training DRL model...")
    model.train_drl(input_data, targets, epochs=10)

    # Preliminary test: Train UPN model
    print("Training UPN model...")
    model.train_upn(input_data, targets, epochs=10)

    # Preliminary test: Make predictions
    test_data = torch.randn(10, input_dim)
    drl_predictions = model.predict_drl(test_data)
    print("DRL Predictions:", drl_predictions)

if __name__ == "__main__":
    main()