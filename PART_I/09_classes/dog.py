class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog setting in response to a command."""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Lu",10)
my_dog.sit()
