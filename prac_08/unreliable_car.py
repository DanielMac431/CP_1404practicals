from prac_08.car import Car
import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(fuel, name)
        self.reliability = reliability

    def drive(self, distance):
        luck = random.randint(1, 101)
        if luck < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
