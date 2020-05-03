import unittest
import sys

sys.path.insert(0, '../src/')

import numpy as np
from math import pi

import mathematics as mts


# general class to test the model

class TestMathematics(unittest.TestCase):
    
    def setUp(self):
        self._x = [1, 0, 0]
        self._y = [0, 1, 0]
        self._z = [0, 0, 1]

    def test_rotation_matrix_3D_xy(self):
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xy(pi/2.), self._x), 10)), \
                self._y)
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xy(pi/2.), self._y), 10)), \
                 [-i for i in self._x])
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xy(pi/2.), self._z), 10)), \
                 self._z)

    def test_rotation_matrix_3D_yz(self):
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_yz(pi/2.), self._x), 10)), \
                self._x)
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_yz(pi/2.), self._y), 10)), \
                self._z)
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_yz(pi/2.), self._z), 10)), \
                [-i for i in self._y])

    def test_rotation_matrix_3D_xz(self):
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xz(pi/2.), self._x), 10)), \
                [-i for i in self._z])
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xz(pi/2.), self._y), 10)), \
                self._y)
        self.assertListEqual(list(np.around(np.dot(mts.rotation_matrix_3D_xz(pi/2.), self._z), 10)), \
                self._x)



if __name__ == '__main__':
    unittest.main()

