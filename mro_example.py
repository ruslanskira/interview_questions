import unittest

class Vehicle:
    def __init__(self):
        self.name = "Vehicle"

    def get_info(self):
        return f"This is a {self.name}"

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = "Car"

    def get_info(self):
        return f"{super().get_info()} and it is a {self.name}"

class ElectricCar(Car):
    def __init__(self):
        super().__init__()
        self.name = "Electric Car"

    def get_info(self):
        return f"{super().get_info()} powered by electricity"

class TestVehicle(unittest.TestCase):
    def test_get_info(self):
        vehicle = Vehicle()
        self.assertEqual(vehicle.get_info(), "This is a Vehiclee")

    def test_car_get_info(self):
        car = Car()
        self.assertEqual(car.get_info(), "This is a Car and it is a Car")

    def test_electric_car_get_info(self):
        electric_car = ElectricCar()
        self.assertEqual(electric_car.get_info(), "This is a Electric Car and it is a Electric Car powered by electricity")

if __name__ == "__main__":
    unittest.main()