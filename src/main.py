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

    model = Model(input_dim, output_dim, context="professional")
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
    print("DRL Predictions:", drl_predictions)

    # Example usage of NLPProcessor
    nlp_processor = model.nlp_processor
    message = "Apple is looking at buying U.K. startup for $1 billion"
    print("Processing message:", message)
    nlp_processor.process_message(message)

if __name__ == "__main__":
    main()