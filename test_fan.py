# Import Fan from fan
from fan import Fan

class TestFan:
    # Define class TestFan
    def run_test(self):
        # Create two Fan objects
        fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        # Display properties of the first fan
        print("\033[1mFAN 1\033[0m")
        print("\033[93mFan 1 - Speed:", fan1.get_speed(), "\033[0m")
        print("\033[93mFFan 1 - Radius:", fan1.get_radius(), "\033[0m")
        print("\033[93mFFan 1 - Color:", fan1.get_color(), "\033[0m")
        print("\033[93mFFan 1 - On:", fan1.is_on(), "\033[0m")
        print("")

        # Display properties of the second fan
        print("\033[1mFAN 2\033[0m")
        print("\033[94mFFan 2 - Speed:", fan2.get_speed(), "\033[0m")
        print("\033[94mFan 2 - Radius:", fan2.get_radius(), "\033[0m")
        print("\033[94mFan 2 - Color:", fan2.get_color(), "\033[0m")
        print("\033[94mFan 2 - On:", fan2.is_on(), "\033[0m")

# Create an instance  of the TestFan and run the test
test = TestFan()
test.run_test()