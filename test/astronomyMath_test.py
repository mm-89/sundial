import unittest
import sys

sys.path.insert(0, '../src/')

import numpy as np

import astronomyMath as am

# current value to test
year = 2012

# external data
file_solar_declination_angle = "solar_declination_angle.txt"
file_equation_of_time = "equation_of_time.txt"

#try to load all external file
try:
    solar_declination_angle_external = list(np.loadtxt(file_solar_declination_angle))
    equation_of_time_external = list(np.loadtxt(file_equation_of_time))
except IOError:
    print("Impossible to open the file")

# general class to test the model

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        self.vector_days = [i for i in range(365)]
        self.year = year
        self.solar_declination_angle = [am.solar_declination_angle(year, i) \
                for i in self.vector_days]
        self.equation_of_time = [am.equation_of_time(year, i) \
                for i in self.vector_days]

        self.solar_declination_angle_external = solar_declination_angle_external
        self.equation_of_time_external = equation_of_time_external

    def test_solar_declination_angle(self):
        self.assertListEqual(self.solar_declination_angle, \
                self.solar_declination_angle_external)

    def test_equation_of_time(self):
        self.assertListEqual(self.equation_of_time, \
                self.equation_of_time_external)




if __name__ == '__main__':
    unittest.main()

