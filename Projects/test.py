class Car:
    """
    This class represents a car with properties like color, model, and company.
    It also has a method 'drive' to simulate driving the car.
    """
    def __init__(self, color, model, company):
        self._color = color
        self._model = model
        self._company = company

    """
    Getter method to get the color of the car.
    :return: str, color of the car
    """
    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        """
        Sets the color of the object.

        Args:
            value (str): The new color value.

        Raises:
            ValueError: If the color value is empty.

        Example:
        >> obj = MyObject()
        >> obj.color = "red"  # sets the color to red
        > obj.color = ""  # raises ValueError: Color cannot be empty
        """
        if value != "":
            self._color = value
        else:
            raise ValueError("Color cannot be empty")

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, value):
        self._company = value

    def drive(self):
        print("Driving the car")


# Create an object of the class
car = Car("Red", "Sedan", "Toyota")

# Demonstrate the use of the getters and setters
print("Color:",car.color)  # Output: Red
car.color = "Blue"
print(car.color)  # Output: Blue

print("Model:",car.model)  # Output: Sedan
car.model = "SUV"
print(car.model)  # Output: SUV

print("Company:",car.company)  # Output: Toyota
car.company = "Honda"
print(car.company)  # Output: Honda

car.drive()  # Output: Driving the car

