from math import cos, sin
import numpy as np

def rotation_matrix_3D_xy(angle):
	"""
	Classical rotational 3D matrix around z-axis
	of angle "angle" (counterclockwise)
	"""
	return np.array([[cos(angle), -sin(angle), 0],
			[sin(angle), cos(angle), 0],
		        [0, 0, 1]])

def rotation_matrix_3D_yz(angle):
	"""
	Classical rotational 3D matrix around x-axis
	of angle "angle" (counterclockwise)
	"""
	return np.array([[1, 0, 0],
			[0, cos(angle), -sin(angle)],
			[0, sin(angle), cos(angle)]])


def rotation_matrix_3D_xz(angle):
	"""
	Classical rotational 3D matrix around y-axis
	of angle "angle" (counterclockwise)
	"""
	return np.array([[cos(angle), 0, sin(angle)],
			[0, 1, 0],
			[-sin(angle), 0, cos(angle)]])
