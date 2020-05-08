from math import cos, sin, pi

import numpy as np

from astronomyMath import solar_declination_angle as sda
from mathematics import *


class Sundial:

    def __init__(self,
                lat,
                lon,
                h,
                alpha,
                beta,
                lamb,
                gamma,
                ):
        
        self.lat = lat
        self.lon = lon

        self.h = h

        self.alpha = alpha
        self.beta = beta
        self.lamb = lamb
        self.gamma = gamma
   

    def set_days_to_plot(self, days):
        self.days = days

    def make_sundial(self):


def sun_direction(year, day, lat, time_loc):
    """
    Ref: Sproul 2006
    """
    
    # change the time hour. The max is time_loc = 12
    # To check this formula
    H_a = (2 * pi * time_loc) / 24. -pi

    #compute S in components
    Sx = -cos(sda(year, day)) * sin(H_a)
    Sy = sin(sda(year, day)) * cos(lat) - \
           cos(sda(year, day)) * sin(lat) *cos(H_a)
    Sz = cos(sda(year, day)) * cos(lat) * cos(H_a) + \
           sin(sda(year, day)) * sin(lat)
    
    return np.array([Sx, Sy, Sz])
    
def sun_direction_on_inclined_plane(year, day, lat, time_loc, alpha, beta):
	"""
	sun is rotated istead of the plane
	"""
	#rotation on x axis .. TO VERIFY
	rot_x_alpha = np.dot(rotation_matrix_3D_yz(alpha), 
				sun_direction(year, day, lat, time_loc))
	#rotation on y axis .. TO VERIFY
	#note: this is declination of the wall
	rot_y_beta = np.dot(rotation_matrix_3D_xz(beta),
					rot_x_alpha)
					
	return rot_y_beta
				
	
def simple_shadow_projection((year, day, lat, time_loc, h):
	"""
	projection with vertical gnomon
	"""
	x_proj = - h * sun_direction(year, day, lat, time_loc)[0] / \
					sun_direction(year, day, lat, time_loc)[2]
					
	y_proj = - h * sun_direction(year, day, lat, time_loc)[1] / \
					sun_direction(year, day, lat, time_loc)[2]
					
	return np.array([x_proj, y_proj])
