# Bernabe,Aleckxis Kate V.
# BSCpE 1-4

# Pet class represents pet data
class Pet:
    # Initialize private data attributes for name, animal type, and age
    def __init__(self):
        self.__name = ""
        self.__animal_type = ""
        self.__age = 0

    # Set the value of the name attribute
    def set_name(self, name):
        self.__name = name

    # Set the value of the animal_type attribute
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Set the value of the age attribute
    def set_age(self, age):
        self.__age = age

    # Return the value of the name attribute
    def get_name(self):
        return self.__name

    # Return the value of the animal_type attribute
    def get_animal_type(self):
        return self.__animal_type

    # Return the value of the age attribute
    def get_age(self):
        return self.__age