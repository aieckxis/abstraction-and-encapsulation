# Import Fan from fan
from fan import Fan

class TestFan:
    # Define class TestFan
    def run_test(self):
        # Create two Fan objects
        fan1 = Fan(Fan.FAST, 10, 'yellow', True)
        fan2 = Fan(Fan.MEDIUM, 5, 'blue', False)

        # Display properties of the first fan
        # Display properties of the second fan

# Create an instance  of the TestFan and run the test
test = TestFan()
test.run_test()