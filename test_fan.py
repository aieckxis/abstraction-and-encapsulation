# Import Fan from fan
from fan import Fan

class TestFan:
    # Define class TestFan
    def run_test(self):
        # Create two Fan objects
        fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        # Display properties of the first fan
        print("Fan 1 - Speed:", fan1.get_speed())
        print("Fan 1 - Radius:", fan1.get_radius())
        print("Fan 1 - Color:", fan1.get_color())
        print("Fan 1 - On:", fan1.is_on())

        # Display properties of the second fan

# Create an instance  of the TestFan and run the test
test = TestFan()
test.run_test()