import unittest
import sys

sys.path.insert(0, '../src/')

import sundial
import check_param

lat = '+46-55-30'
lon =  '13-49-59'

angle_case = 43.5

day_to_plot = '21 21 21 21 21 21 21 21 21 21 21 21'
mon_to_plot = '1 1 1 1 1 1 1 1 1 1 1 1'

class TestStringMethods(unittest.TestCase):

    def test_trans_degree_decimal_lat(self):
        self.assertEqual(\
                check_param.trans_degree_decimal_lat(lat), 46.925)
    def test_trans_degree_decimal_lon(self):
        self.assertEqual(\
                check_param.trans_degree_decimal_lon(lon), 13.833055555555555)

    def test_type_and_len_coordinates_lat(self):
        self.assertEqual(\
                check_param.check_type_and_len_coordinates_lat(lat), True)
    def test_type_and_len_coordinates_lon(self):
        self.assertEqual(\
                check_param.check_type_and_len_coordinates_lon(lon), True)

    def test_coordinates_lat(self):
        self.assertEqual(\
                check_param.check_dimension_coordinates_lat(lat), True)
    def test_coordinates_lon(self):
        self.assertEqual(\
                check_param.check_dimension_coordinates_lon(lon), True)

    def test_transform_degree_to_radiant(self):
        self.assertEqual( \
                check_param.trans_degree_to_radiant(angle_case), 0.7592182246175333)
    
    def test_tranform_days(self):
        self.assertEqual( \
                check_param.transform_days(day_to_plot), \
                [21.0, 52.0, 80.0, 111.0, 141.0, 172.0, 202.0, 233.0, 264.0, 294.0, 325.0, 355.0])
    
    def test_tranform_month(self):
        self.assertEqual( \
                check_param.transform_month(mon_to_plot), \
                [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0 , 1.0, 1.0, 1.0])




if __name__ == '__main__':
    unittest.main()

