# Import the Car from car.py
from car import Car

# Main function to test the Car class
def main():
    car = Car(2003, "Mercedes-Benz")
    # Print the initial speed of the car
    print("\033[1mInitial speed: ", car.get_speed(), "\033[0m")
    print("")

    # Accelerate the car five times
    for _ in range(5):
        car.accelerate()
        print("\033[32mCurrent speed after accelerating:", car.get_speed(), "\033[0m")

    print("")
    # Brake the car five times
    for _ in range(5):
        car.brake()
        print("\033[31mCurrent speed after braking:", car.get_speed(), "\033[0m")

# Check if the current file is the main file being executed
if __name__ == "__main__":
    main()
