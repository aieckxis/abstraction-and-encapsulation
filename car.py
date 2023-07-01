# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

# Car class represents a car object
class Car:
    # Constructor to initialize the car's year model, make, and speed
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Method to accelerate the car's speed by 5
    def accelerate(self):
        # Increase the car's speed by 5
        self.__speed += 5

    # Method to brake and decrease the car's speed by 5 units
    def brake(self):
        # Decrease the car's speed by 5
        self.__speed -= 5

    # Method to get the current speed of the car
    def get_speed(self):
        return self.__speed