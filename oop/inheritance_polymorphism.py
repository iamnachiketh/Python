class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting....")

    def stop(self):
        print("Vehicle is stopping....")
    

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors


class Bike(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears
    
    def start(self): # Overriding the start method
        print("Bike is starting....")

    def stop(self): # Overriding the stop method
        print("Bike is stopping....")


car = Car("Toyota", "Corolla", 2019, 4)
bike = Bike("Honda", "CBR", 2020, 6)

car.start()
car.stop()
print(car.__dict__) # {'make': 'Toyota', 'model': 'Corolla', 'year': 2019, 'num_doors': 4}

bike.start()
bike.stop()
print(bike.__dict__) # {'make': 'Honda', 'model': 'CBR', 'year': 2020, 'num_gears': 6}


vehicle_list = [
    Car("Toyota", "Corolla", 2019, 4),
    Bike("Honda", "CBR", 2020, 6)
]

for vehicle in vehicle_list:
    vehicle.start()
    vehicle.stop()
    print(vehicle.__dict__)

print(f'Is the car object an instance of Bike: {isinstance(car, Bike)}')

print(f"Type of car object: {type(car).__name__}")



