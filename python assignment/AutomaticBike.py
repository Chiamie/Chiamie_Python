class Bike:
    def __init__(self):
        self.gear = 0
        self.is_on = False
        self.speed = 0

    def power_button(self):
        if not self.is_on:
            self.is_on = True
        else:
            self.is_on = False

    def power(self):
        return self.is_on

    def get_speed(self):
        return self.speed

    def accelerate(self):
        if self.is_on:
            self.speed = self.speed + self.gear
        return "The Bike is off"

    def decelerate(self):
        if self.is_on:
            if self.speed > 0:
                self.speed = self.speed - self.gear
        return "The Bike is off"

    def set_gear(self):
        if self.is_on:
            if 0 <= self.speed <= 20:
                self.gear = 1
            elif 21 <= self.speed <= 30:
                self.gear = 2
            elif 31 <= self.speed <= 40:
                self.gear = 3
            else:
                self.gear = 4