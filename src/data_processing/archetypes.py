import numpy as np # type: ignore

class ArchetypeBlender:
    def __init__(self):
        self.archetypes = {
            "Mother Earth": {"weight": 10, "traits": np.array([0.9, 0.9, 0.9, 0.9])},
            "Hero": {"weight": 10, "traits": np.array([0.9, 0.8, 0.7, 0.8])},
            "Sage": {"weight": 9, "traits": np.array([0.8, 0.9, 0.7, 0.8])},
            "Ruler": {"weight": 8, "traits": np.array([0.7, 0.8, 0.9, 0.7])},
            "Creator": {"weight": 8, "traits": np.array([0.9, 0.7, 0.8, 0.9])},
            "Caregiver": {"weight": 7, "traits": np.array([0.8, 0.7, 0.9, 0.7])},
            "Magician": {"weight": 7, "traits": np.array([0.7, 0.9, 0.8, 0.8])},
            "Lover": {"weight": 6, "traits": np.array([0.9, 0.8, 0.6, 0.7])},
            "Jester": {"weight": 6, "traits": np.array([0.8, 0.6, 0.9, 0.7])},
            "Everyman": {"weight": 5, "traits": np.array([0.7, 0.7, 0.7, 0.8])},
            "Innocent": {"weight": 5, "traits": np.array([0.9, 0.6, 0.7, 0.8])},
            "Explorer": {"weight": 4, "traits": np.array([0.6, 0.9, 0.7, 0.7])},
            "Rebel": {"weight": 4, "traits": np.array([0.7, 0.6, 0.9, 0.6])}
        }
        self.total_weight = sum(arch["weight"] for arch in self.archetypes.values())

    def blend_personality(self, context_weights=None):
        if context_weights is None:
            context_weights = {name: 1 for name in self.archetypes}
        
        personality = np.zeros(4)  # Assuming 4 trait dimensions
        for name, archetype in self.archetypes.items():
            weight = archetype["weight"] * context_weights.get(name, 1)
            personality += (weight / self.total_weight) * archetype["traits"]
        
        return personality / np.sum(personality)  # Normalize

    def adjust_for_context(self, context):
        context_weights = {
            "professional": {"Hero": 1.2, "Sage": 1.1, "Ruler": 1.2, "Creator": 1.1},
            "casual": {"Jester": 1.2, "Lover": 1.1, "Everyman": 1.2, "Explorer": 1.1},
            "creative": {"Creator": 1.3, "Magician": 1.2, "Explorer": 1.1, "Rebel": 1.1},
            "ethical_dilemma": {"Sage": 1.3, "Hero": 1.2, "Ruler": 1.1, "Caregiver": 1.1}
        }
        return self.blend_personality(context_weights.get(context, None))

    def assess_individual(self, trait_scores):
        personality = np.zeros(4)
        for name, score in trait_scores.items():
            if name in self.archetypes:
                weight = self.archetypes[name]["weight"] * score / 10  # Normalize score to 0-1
                personality += weight * self.archetypes[name]["traits"]
        return personality / np.sum(personality)  # Normalize

class ArchetypeTraitAnalyzer:
    def __init__(self):
        self.archetypes = {
            "Innocent": {"Optimism": 10, "Childlike wonder": 9, "Trusting": 8, "Purity": 7, "Simplicity": 6},
            "Everyman": {"Relatable": 10, "Empathic": 9, "Adaptable": 8, "Down-to-earth": 7, "Understanding": 6},
            "Hero": {"Courageous": 10, "Determined": 9, "Skilled": 8, "Inspiring": 7, "Self-sacrificing": 6},
            "Caregiver": {"Nurturing": 10, "Compassionate": 9, "Selfless": 8, "Supportive": 7, "Protective": 6},
            "Explorer": {"Adventurous": 10, "Independent": 9, "Curious": 8, "Free-spirited": 7, "Pioneering": 6},
            "Rebel": {"Nonconforming": 10, "Passionate": 9, "Courageous": 8, "Revolutionary": 7, "Defiant": 6},
            "Lover": {"Passionate": 10, "Devoted": 9, "Romantic": 8, "Sensual": 7, "Committed": 6},
            "Creator": {"Innovative": 10, "Creative": 9, "Imaginative": 8, "Expressive": 7, "Artistic": 6},
            "Jester": {"Humorous": 10, "Playful": 9, "Joyful": 8, "Spontaneous": 7, "Entertaining": 6},
            "Sage": {"Wise": 10, "Knowledgeable": 9, "Analytical": 8, "Insightful": 7, "Reflective": 6},
            "Magician": {"Transformative": 10, "Visionary": 9, "Intuitive": 8, "Charismatic": 7, "Influential": 6},
            "Ruler": {"Authoritative": 10, "Powerful": 9, "Responsible": 8, "Strategic": 7, "Commanding": 6}
        }

    def analyze_archetype(self, archetype_name, trait_scores):
        if archetype_name not in self.archetypes:
            raise ValueError(f"Unknown archetype: {archetype_name}")
        
        archetype_traits = self.archetypes[archetype_name]
        total_score = 0
        max_possible_score = sum(archetype_traits.values()) * 10

        for trait, weight in archetype_traits.items():
            if trait in trait_scores:
                total_score += trait_scores[trait] * weight

        percentage = (total_score / max_possible_score) * 100
        return total_score, percentage

    def analyze_personality(self, trait_scores):
        personality_profile = {}
        for archetype in self.archetypes:
            score, percentage = self.analyze_archetype(archetype, trait_scores)
            personality_profile[archetype] = {"score": score, "percentage": percentage}
        return personality_profile


blender = ArchetypeBlender()
default_personality = blender.blend_personality()
professional_personality = blender.adjust_for_context("professional")
creative_personality = blender.adjust_for_context("creative")

print("Default Personality:", default_personality)
print("Professional Context:", professional_personality)
print("Creative Context:", creative_personality)

# Example usage
analyzer = ArchetypeTraitAnalyzer()

# Example trait scores for an individual
individual_traits = {
    "Courageous": 9, "Determined": 8, "Skilled": 7, "Inspiring": 6, "Self-sacrificing": 5,  # Hero traits
    "Wise": 8, "Knowledgeable": 7, "Analytical": 9, "Insightful": 8, "Reflective": 7,  # Sage traits
    "Innovative": 9, "Creative": 8, "Imaginative": 9, "Expressive": 7, "Artistic": 6  # Creator traits
}

personality_profile = analyzer.analyze_personality(individual_traits)

# Print results
for archetype, data in personality_profile.items():
    print(f"{archetype}: Score = {data['score']}, Percentage = {data['percentage']:.2f}%")
