import math

class DecisionController:

    def __init__(self):
        self.initial_speed = 0
        self.acceleration_positive = 0
        self.acceleration_negative = 0
        self.distance_all = 0
        self.distance = 0
        self.yellow_light_duration = 0

    def make_decision(self, car, intersection):
        self.initial_speed = car.initial_speed
        self.acceleration_positive = car.acceleration_positive
        self.acceleration_negative = car.acceleration_positive
        car_distance = car.initial_distance
        self.distance = car_distance
        intersection_width = intersection.width
        self.distance_all = car_distance + intersection_width
        self.yellow_light_duration = intersection.yellow_light_duration
        suggestion = self.calculate_decision()
        return suggestion

    def calculate_time_needed_accelerating(self, acceleration):
        time = ((-1*self.initial_speed) + (math.sqrt((pow(self.initial_speed, 2) + 2 * acceleration * self.distance_all)))) / acceleration
        return time

    def calculate_time_needed_decelerating(self, acceleration):
        time = (self.initial_speed - (math.sqrt((pow(self.initial_speed, 2) - 2 * acceleration * self.distance)))) / acceleration
        return time

    def calculate_decision(self):
        # First try accelerating
        time_needed = self.calculate_time_needed_accelerating(self.acceleration_positive)
        time_needed_dec = self.calculate_time_needed_decelerating(self.acceleration_negative)

        if time_needed < self.yellow_light_duration:
            if time_needed_dec > self.yellow_light_duration:
                return "You Need to Accelerate"
            else:
                return "You can either Accelerate or Decelerate"
        elif time_needed_dec < self.yellow_light_duration:
            return "You Need to Decelerate"
        else:
            return "You cannot nor accelerate nor decelerate"



