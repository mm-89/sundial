import unittest
import sundial

year = 2000
day = 108
degree = 45
time = 3600 # 1 p.m. ideally
h = 0.5

class TestStringMethods(unittest.TestCase):

	def test_solar_zenith_angle(self):
		self.assertEqual(sundial.solar_zenith_angle(year,day,degree,time),0.7996494169677558)

	def test_get_b(self):
		self.assertEqual(sundial.get_b(year,day,degree,time,h),0.3754565106987939)



if __name__ == '__main__':
    unittest.main()

