class Vehicle:
    def move(self):

# Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Testing Polymorphism
vehicle1 = Car()
vehicle2 = Plane()

vehicle1.move()  # Outputs: Driving 🚗
vehicle2.move()  # Outputs: Flying ✈️
