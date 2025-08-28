# Base class
class Vehicle:
    def move(self):
        pass  # Placeholder for polymorphism

# Different vehicle classes
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing ⛴️"

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for v in vehicles:
    print(v.move())
