def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(f"Results of **kwargs:\n "
      f"{calculate(2, add=4, multiply=2)}")

class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]
        """
        In case we don't supply an attribute (say model), the code above will enable a
        keyword argument. So we would use the 'get' method to get the car model
        """
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

# my_car = Car(make="Mazda", model="CX-90")
# Testing the get method to avoid errors, not providing an argument
my_car = Car(make="Mazda", color="Ash Gray", seats = 5)
print(f"Making my car: {my_car.make}")
print(f"Car Model: {my_car.model}")
print(f"Car Color: {my_car.color}")
print(f"Car Seats: {my_car.seats}")