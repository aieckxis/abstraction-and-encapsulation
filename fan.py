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