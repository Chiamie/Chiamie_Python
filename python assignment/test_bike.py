import unittest
from AutomaticBike import Bike


class TestThePowerFunction(unittest.TestCase):
    def setUp(self):
        self.bike = Bike()

    def test_that_the_default_state_of_bike_is_off(self):
        self.assertFalse(self.bike.is_on,  False)


    def test_that_the_bike_can_be_turned_on(self):
        self.assertTrue(self.bike.power_button, True)

    def test_that_the_bike_is_at_rest_when_turned_on(self):
        self.bike.power_button()
        self.assertEqual(self.bike.speed, 0)

    def test_that_the_bike_can_be_turned_off(self):
        self.bike.power_button()
        self.bike.power_button()
        self.assertFalse(self.bike.power(),  False)

    def test_that_the_bike_accelerates_when_turned_on(self):
        self.bike.power_button()
        self.bike.set_gear()
        self.bike.accelerate()
        self.assertEqual(self.bike.get_speed(), 1)

    def test_that_the_bike_doesnt_accelerate_when_turned_off(self):
        self.assertEqual(self.bike.accelerate(), "The Bike is off")

    def test_that_the_bike_decelerates_when_turned_on(self):
        self.bike.power_button()
        self.bike.set_gear()
        self.bike.accelerate()
        self.bike.decelerate()
        self.assertEqual(self.bike.get_speed(), 0)

    def test_that_the_bike_doesnt_decelerate_when_turned_off(self):
        self.assertEqual(self.bike.decelerate(), "The Bike is off")

    def test_that_when_speed_is_zero_it_cannot_decelerate(self):
        self.bike.power_button()
        self.bike.set_gear()
        self.bike.decelerate()
        self.assertEqual(self.bike.get_speed(), 0)



if __name__ == '__main__':
    unittest.main()
