from math import cos, sin, pi

import numpy as np

from astronomyMath import solar_declination_angle as sda
from mathematics import *

from checkNamelist import CheckNamelist
from readNamelist import ReadNamelist
from parameters import Parameters



class Sundial(Parameters, CheckNamelist, ReadNamelist):

    def sunRaysDirection(self, year, day, lat, time_loc):
        #check "lat" variable, probably to delete it
        """
        Ref: Sproul 2006
        """
        
        # change time from hour to radiant
        H_a = pi * (time_loc/12. - 1)

        #compute S in components
        sx = -cos(sda(year, day)) * sin(H_a)

        sy = sin(sda(year, day)) * cos(lat) - \
               cos(sda(year, day)) * sin(lat) *cos(H_a)

        sz = cos(sda(year, day)) * cos(lat) * cos(H_a) + \
               sin(sda(year, day)) * sin(lat)
        
        return sx, sy, sz

    def horizontalPlane(self, gamma, psi, h, year, day, lat, time_loc):
        #check "h" variable, probably to delete it

         # change time from hour to radiant
        H_a = pi * (time_loc/12. - 1)
        
        x = h * sin(gamma) * cos(psi) - \
            (self.sunRaysDirection(year, day, lat, time_loc)[0] - h * sin(gamma) * cos(psi)) * \
            h * cos(gamma) / self.sunRaysDirection(year, day, lat, time_loc)[2]

        y = h * sin(gamma) * sin(psi) - \
            (self.sunRaysDirection(year, day, lat, time_loc)[1] - h * sin(gamma) * sin(psi)) * \
            h * cos(gamma) / self.sunRaysDirection(year, day, lat, time_loc)[2]

        return x, y
