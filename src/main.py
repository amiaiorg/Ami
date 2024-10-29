from models.model import Model
from data_sources.archetypes import ArchetypeBlender
from data_sources.user_neural_pattern import UserNeuralPattern
import torch

def main():
    print("Welcome to AMI")

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
    input_dim = 10
    output_dim = 2
    azure_config = {
        "subscription_id": "your_subscription_id",
        "resource_group": "your_resource_group",
        "workspace_name": "your_workspace_name",
        "compute_name": "your_compute_name"
    }

    model = Model(input_dim, output_dim, context="professional", azure_config=azure_config)
    data = torch.randn(100, input_dim)
    targets = torch.randn(100, output_dim)

    # Preliminary test: Train DRL model
    print("Training DRL model...")
    model.train_drl(data, targets, epochs=10)

    # Preliminary test: Train UPN model
    print("Training UPN model...")
    model.train_upn(data, targets, epochs=10)

    # Preliminary test: Make predictions
    test_data = torch.randn(10, input_dim)
    drl_predictions = model.predict_drl(test_data)
    upn_predictions = model.predict_upn(test_data)
    print("DRL Predictions:", drl_predictions)
    print("UPN Predictions:", upn_predictions)

    # Apply ethical principles
    context = {}
    context = model.apply_ethics("Mentalism", context)
    context = model.apply_ethics("Correspondence", context)
    context = model.apply_ethics("Vibration", context)
    context = model.apply_ethics("Polarity", context)
    context = model.apply_ethics("Rhythm", context)
    context = model.apply_ethics("Cause and Effect", context)
    context = model.apply_ethics("Gender", context)
    context = model.apply_fools_wisdom(context)
    print("Ethical Context:", context)

    # If using Azure ML, run a test training job
    if model.azure_ml_handler:
        script_path = "path/to/your/training_script.py"
        script_args = ["--arg1", "value1", "--arg2", "value2"]
        environment_name = "your_environment_name"
        print("Running training on Azure ML...")
        run = model.train_model_on_azure(script_path, script_args, environment_name)
        print("Azure ML run completed:", run)

if __name__ == "__main__":
    main()