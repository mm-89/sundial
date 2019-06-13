import sys
from math import *

sys.path.insert(0, '../')

from namelist import *

# function definitions ---------------------------------------------

def trans_degree_decimal(long_val):
	"""
	Some definition
	"""
	if(long_val==lon):
		new_val = float(long_val[0:2]) + float(long_val[3:5]) / 60. +\
		float(long_val[5:7]) / 3600.

	if(long_val==lat):
		new_val = float(long_val[1:3]) + float(long_val[4:6]) / 60. +\
		float(long_val[7:9]) / 3600.
		if(long_val[0]=='-'):
			new_val = - new_val

	return new_val

def trans_degree_radiant(angle):
	"""
	Some definition
	"""
	new_angle = angle * pi / 180.
	
	return new_angle

def check_type_and_len_coordinates(param):
	"""
	note: 
			true = ok
			false = there's a problema
	"""

	verify = True
	if(param==lat):
		if( not type(param) is str):
			verify = False
		if( not len(param) is 9):
			verify = False

	if(param==lon):
		if( not type(param) is str):
			verify = False
		if( not len(param) is 8):
			verify = False

	return verify

def check_dimension_coordinates(long_val):
	"""
	note:
			true: ok
			false: there's a problem
	"""
	verify = True
	if(long_val==lon):
		degree = float(long_val[0:2])
		minute = float(long_val[3:5]) 
		second = float(long_val[6:8])

		if(degree < 0. or degree > 360.):
			verify = False
		if(minute < 0. or minute > 60.):
			verify = False
		if(second < 0. or second > 60.):
			verify = False

	if(long_val==lat):
		degree = float(long_val[1:3])
		minute = float(long_val[4:6]) 
		second = float(long_val[7:9])

		if(degree < 0. or degree > 90.):
			verify = False
		if(minute < 0. or minute > 60.):
			verify = False
		if(second < 0. or second > 60.):
			verify = False
	return verify


# check parameters namelist --------------------------------------
