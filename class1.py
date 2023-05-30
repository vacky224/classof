class Car:
    def __init__(self, make, model,color):
        self.make = make
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.make} {self.model} which is a {self.color} car is driving.")

# Creating objects of the Car class
car1 = Car("Toyota", "Camry","Red")
car2 = Car("Ford", "Mustang", "Yellow")

# Accessing attributes and calling methods
print(car1.make)     # Output: Toyota
print(car2.model)    # Output: Mustang
print(car2.color)

car1.drive()         # Output: The Toyota Camry is driving.
car2.drive()         # Output: The Ford Mustang is driving.

