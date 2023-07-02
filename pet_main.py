# Import Pet from pet
from pet import Pet

# Main function to test the Pet class
def main():

    # Create an instance for Pet class
    pet = Pet()

    # Ask the user for pet's information
    name = input("Enter the name of your pet: ")
    pet.set_name(name)

    animal_type = input("Enter the type of animal your pet is: ")
    pet.set_animal_type(animal_type)

    age = input("Enter the age of your pet: ")
    pet.set_age(age)

    # Print the pet's information
    print("")
    print("\033[1mPET'S INFORMATION\033[0m")
    print("Pet's name: ", pet.get_name())
    print("Animal type: ", pet.get_animal_type())
    print("Pet's age: ", pet.get_age())

# Check if the current file is the main file being executed
if __name__ == "__main__":
    main()