from math import cos, sin, pi

import matplotlib.pyplot as plt

import numpy as np

from astronomyMath import solar_declination_angle as sda
from mathematics import *

from checkNamelist import CheckNamelist
from readNamelist import ReadNamelist
from parameters import Parameters



class Sundial(Parameters, CheckNamelist, ReadNamelist):


    def sunRaysDirection(self, day, time_loc):
        #check "lat" variable, probably to delete it
        """
        Ref: Sproul 2006
        """
        
        # change time from hour to radiant
        H_a = pi * (time_loc/12. - 1)

        #compute S in components
        sx = -cos(sda(self.year, day)) * sin(H_a)

        sy = sin(sda(self.year, day)) * cos(self.lat_p) - \
               cos(sda(self.year, day)) * sin(self.lat_p) *cos(H_a)

        sz = cos(sda(self.year, day)) * cos(self.lat_p) * cos(H_a) + \
               sin(sda(self.year, day)) * sin(self.lat_p)
        
        return sx, sy, sz


    def horizontalPlane(self, day, time_loc):
        #check "h" variable, probably to delete it

         # change time from hour to radiant
        H_a = pi * (time_loc/12. - 1)

        thisRay = self.sunRaysDirection
        """
        x = self.h_p * sin(self.gamma_p) * cos(self.lamb_p) - \
            (thisRay(day, time_loc)[0] - self.h_p * sin(self.gamma_p) * cos(self.lamb_p)) * \
            self.h_p * cos(self.gamma_p) / thisRay(day, time_loc)[2]

        y = self.h_p * sin(self.gamma_p) * sin(self.lamb_p) - \
            (thisRay(day, time_loc)[1] - self.h_p * sin(self.gamma_p) * sin(self.lamb_p)) * \
            self.h_p * cos(self.gamma_p) / thisRay(day, time_loc)[2]
        """

        x = self.h_p * thisRay(day, time_loc)[0] / thisRay(day, time_loc)[2]
        y = self.h_p * thisRay(day, time_loc)[1] / thisRay(day, time_loc)[2]

        return x, y


    def showSundial(self):
        #row is month
        #column is hour
           
        for i, item in enumerate(self.cum_days_to_plot):

            x_dial = []
            y_dial = []

            for j, comp in enumerate(self.hours_per_day):

                tmp_x = self.horizontalPlane(item, comp)[0]
                tmp_y = self.horizontalPlane(item, comp)[1]

                if( (tmp_x<float(self.max_dial_x) and tmp_x>-float(self.max_dial_x)) and \
                    (tmp_y<float(self.max_dial_y) and tmp_y>-float(self.max_dial_y)) ):
                    x_dial.append( tmp_x )
                    y_dial.append( tmp_y )

            plt.plot(x_dial, y_dial, label=self.mon_show[i])
        
        plt.legend()
        plt.axis("equal")
        plt.show()
