

class Personality:
    # A class that represents a person's personality based on the Big Five traits

    # Define the class attributes that are common for all personalities
    traits = ["openness", "conscientiousness", "extraversion", "agreeableness", "neuroticism"]

    # Define the instance attributes that are specific for each personality
    def __init__(self, openness = 50, conscientiousness = 50, extraversion = 50, agreeableness = 50, neuroticism = 50):
        # Initialize the values of the Big Five traits for the personality
        # Each value is a number between 0 and 100 that indicates the level of the trait
        self.openness = openness
        self.conscientiousness = conscientiousness
        self.extraversion = extraversion
        self.agreeableness = agreeableness
        self.neuroticism = neuroticism

    # Define some instance methods that describe the characteristics of the personality
    def describe(self):
        # A method that returns a string with the description of the personality based on the Big Five traits
        description = "This personality is "
        # For each trait, add a descriptive adjective based on the level of the trait
        if self.openness > 80:
            description += "very creative, curious, and adventurous. "
        elif self.openness > 60:
            description += "somewhat creative, curious, and adventurous. "
        elif self.openness > 40:
            description += "neither creative nor conventional, neither curious nor indifferent, neither adventurous nor cautious. "
        elif self.openness > 20:
            description += "somewhat conventional, indifferent, and cautious. "
        else:
            description += "very conventional, indifferent, and cautious. "

        if self.conscientiousness > 80:
            description += "very organized, responsible, and hard-working. "
        elif self.conscientiousness > 60:
            description += "somewhat organized, responsible, and hard-working. "
        elif self.conscientiousness > 40:
            description += "neither organized nor messy, neither responsible nor careless, neither hard-working nor lazy. "
        elif self.conscientiousness > 20:
            description += "somewhat messy, careless, and lazy. "
        else:
            description += "very messy, careless, and lazy. "

        if self.extraversion > 80:
            description += "very sociable, energetic, and outgoing. "
        elif self.extraversion > 60:
            description += "somewhat sociable, energetic, and outgoing. "
        elif self.extraversion > 40:
            description += "neither sociable nor shy, neither energetic nor quiet, neither outgoing nor reserved. "
        elif self.extraversion > 20:
            description += "somewhat shy, quiet, and reserved. "
        else:
            description += "very shy, quiet, and reserved. "

        if self.agreeableness > 80:
            description += "very friendly, cooperative, and compassionate. "
        elif self.agreeableness > 60:
            description += "somewhat friendly, cooperative, and compassionate. "
        elif self.agreeableness > 40:
            description += "neither friendly nor hostile, neither cooperative nor competitive, neither compassionate nor indifferent. "
        elif self.agreeableness > 20:
            description += "somewhat hostile, competitive, and indifferent. "
        else:
            description += "very hostile, competitive, and indifferent. "

        if self.neuroticism > 80:
            description += "very anxious, moody, and insecure. "
        elif self.neuroticism > 60:
            description += "somewhat anxious, moody, and insecure. "
        elif self.neuroticism > 40:
            description += "neither anxious nor calm, neither moody nor stable, neither insecure nor confident. "
        elif self.neuroticism > 20:
            description += "somewhat calm, stable, and confident. "
        else:
            description += "very calm, stable, and confident. "

        return description