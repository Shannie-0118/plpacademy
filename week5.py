# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        return f"I am {self.name}, protecting {self.city} with my power of {self.power}."

# Inherited class
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)  # Call parent constructor
        self.flight_speed = flight_speed  # Extra attribute for flying heroes

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Using the classes
hero1 = Superhero("ShadowStrike", "Invisibility", "NeoCity")
hero2 = FlyingSuperhero("SkyBlade", "Laser Eyes", "NeoCity", 900)

print(hero1.introduce())
print(hero2.introduce())
print(hero2.fly())

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
