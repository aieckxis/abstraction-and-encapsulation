# Import the Car from car.py
from car import Car

# Main function to test the Car class
def main():
    car = Car(2003, "Mercedes-Benz")
    # Print the initial speed of the car
    print("Initial speed: ", car.get_speed())

    # Accelerate the car five times
    for _ in range(5):
        car.accelerate()
        print("Current speed after accelerating:", car.get_speed)
    # Brake the car five times
# Check if the current file is the main file being executed
if __name__ == "__main__":
    main()
