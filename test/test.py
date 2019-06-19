import unittest
import sys

sys.path.insert(0, '../src/')

import sundial
import check_param

lat = '+46-55-30'
lon =  '13-49-12'


class TestStringMethods(unittest.TestCase):

    def test_trans_degree_decimal_lat(self):
        self.assertEqual(check_param.trans_degree_decimal_lat(lat), 46.925)
    def test_trans_degree_decimal_lon(self):
        self.assertEqual(check_param.trans_degree_decimal_lon(lon), 13.81638888888889)

    def test_type_and_len_coordinates_lat(self):
        self.assertEqual(check_param.check_type_and_len_coordinates_lat(lat), True)
    def test_type_and_len_coordinates_lon(self):
        self.assertEqual(check_param.check_type_and_len_coordinates_lon(lon), True)

    def test_coordinates_lat(self):
        self.assertEqual(check_param.check_dimension_coordinates_lat(lat), True)
    def test_coordinates_lon(self):
        self.assertEqual(check_param.check_dimension_coordinates_lon(lon), True)





if __name__ == '__main__':
    unittest.main()

