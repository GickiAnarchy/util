#
#
import random

class Human():
    # A class that represents a human being

    # Define the class attributes that are common for all humans
    species = "Homo sapiens"
    is_alive = True
    body_parts = [
    "head", 
    "torso", 
    "right_arm", 
    "left_arm", 
    "right_hand", 
    "left_hand",
    "right_leg", 
    "left_leg", 
    "right_foot", 
    "left_foot"
    ]
    emotions = ["happy", "sad", "angry", "fearful", "surprised", "disgusted"]

    # Define the instance attributes that are specific for each human
    def __init__(self, name = "none", gender = "none", age = 40, strength = 50, health = 100, mental_health = 100, is_alive = True):
        # Initialize the name, gender, age, strength,  and mental health of the human
        self.name = name
        self.gender = gender
        self.age = age
        self.strength = strength # A number between 0 and 100 that indicates the physical power of the human
        self.health = health # A number between 0 and 100 that indicates the physical well-being of the human
        self.mental_health = mental_health # A number between 0 and 100 that indicates the psychological well-being of the human


    def create(self):
      print("Create a person:\n")
      self.name = input("Name? ")
      self.gender = None
      while True:
        self.gender = input("Gender? ")
        if self.gender in ["Male","male","m","M"]:
          self.gender = "Male"
          break
        if self.gender in ["Female","female","F","f"]:
          self.gender = "Female"
          break
      self.age = int(input("Age? "))
      print(self.introduce())
      print(f"{self.name} was created!\n")

    # Define some instance methods that describe the actions of the human
    def introduce(self):
        # A method that returns a string with the name, gender and age of the human
        return f"Hello, my name is {self.name}. I am a {self.gender} and I am {self.age} years old."

    def express(self, emotion):
        # A method that takes an emotion as an argument and returns a string with the human's expression
        if emotion in self.emotions:
            return f"I am feeling {emotion} right now."
        else:
            return f"I don't know how to feel {emotion}."

    def grow(self, years = 1):
        # A method that takes a number of years as an argument and increases the age of the human by that amount
        self.age += years
        return f"I am now {self.age} years old."

    def exercise(self, minutes):
        # A method that takes a number of minutes as an argument and increases the strength and health of the human by a certain amount
        self.strength += minutes * 0.1 # Assume that every minute of exercise increases the strength by 0.1
        self.health += minutes * 0.2 # Assume that every minute of exercise increases the health by 0.2
        # Make sure that the strength and health do not exceed 100
        self.strength = min(self.strength, 100)
        self.health = min(self.health, 100)
        return f"I have exercised for {minutes} minutes. My strength is now {self.strength} and my health is now {self.health}."

    def relax(self, minutes):
        # A method that takes a number of minutes as an argument and increases the mental health of the human by a certain amount
        self.mental_health += minutes * 0.1 # Assume that every minute of relaxation increases the mental health by 0.1
        # Make sure that the mental health does not exceed 100
        self.mental_health = min(self.mental_health, 100)
        return f"I have relaxed for {minutes} minutes. My mental health is now {self.mental_health}."
      
    def checkHealth(self):
      #Check health, returns True if health is above 0.
      if self.health <= 0:
        #Human dies
        is_alive = False
        return False
      else:
        return True
 
    def checkAlive(self):
      #A method that returns whether or not the human is alive.
      if is_alive == True:
        return True
      else:
        return False
 
    def attack(self):
      #Method to return an attack value depending on human health. 
      ap = self.strength/2
      if self.health < 50:
        return random(0,ap/2)
      else:
        return random(ap/2,ap)