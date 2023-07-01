# Bernabe, Aleckxis Kate V.
# BSCpE 1-4

class Fan:
    # Constants for fan speed
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=1, radius=1, color='blue', on=False):
        # Constructor to initialize the Fan object
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = 1

    # Getters and setters for all data fields
    def get_speed(self):
        # Getter method to return the speed value
        return self.speed

    def set_speed(self):
        # Setter method to set the speed value
        self.speed = speed

    def get_radius(self):
        # Getter method to return the radius value
        return self.radius

    def set_radius(self):
        # Setter method to set the radius value
        self.radius = radius

    def get_color(self):
        # Getter method to return the color value
        return self.color

    def set_color(self):
        # Setter method to set the color value
        self.color = color

    def is_on(self):
        # Getter method to check if the fan is on
        return self.on

    def set_on(self):
        # Setter method to turn the fan on or off
        self.on = on