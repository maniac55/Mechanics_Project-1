from desicion_controller import DecisionController
from random import randrange


class car:

    def __init__(self):
        self.initial_speed_can_be = (20, 81)
        self.initial_distance_can_be = (10, 150)
        self.car_acceleration_positive_can_be = (1, 4)
        self.car_acceleration_negative_can_be = (1, 4)
        self.initial_speed_is = 0
        self.initial_distance_is = 0
        self.acceleration_positive_is = 0
        self.acceleration_negative_is = 0

    def define_randomly(self):
        self.initial_speed_is = randrange(*self.initial_speed_can_be)
        self.initial_distance_is = randrange(*self.initial_distance_can_be)
        self.acceleration_positive_is = randrange(*self.car_acceleration_positive_can_be)
        self.acceleration_negative_is = randrange(*self.car_acceleration_negative_can_be)
        self.initial_speed_is = randrange(*self.initial_speed_can_be)


class intersect:
    def __init__(self):
        self.intersection_can_be = (5, 21)
        self.yellow_light_duration_can_be = (2, 6)
        self.widthIs = 0
        self.yellow_light_durationIs = 0

    def define_randomly(self):
        self.widthIs = randrange(*self.intersection_can_be)
        self.yellow_light_durationIs = randrange(*self.yellow_light_duration_can_be)

class main_code:
    def __init__(self):
        # Create Car
        self.car = car()
        self.intersection = intersect()
        self.decision_controller = DecisionController()
        self.car.define_randomly()
        self.intersection.define_randomly()

    def make_decision(self):
        return self.decision_controller.make_decision(car=self.car, intersection=self.intersection)


if __name__ == "__main__":
    control = main_code()
    decision = control.make_decision()

