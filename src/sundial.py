from math import cos, sin, pi

import matplotlib.pyplot as plt

import numpy as np

from astronomyMath import solar_declination_angle as sda
from mathematics import *

from checkNamelist import CheckNamelist
from readNamelist import ReadNamelist
from parameters import Parameters



class Sundial(CheckNamelist, ReadNamelist):

    lat_lenght = [8, 9]
    lon_lenght = [8, 9, 10]

    angles_lenght = [2, 3]

    mon_list_lenght = 23
    day_list_lenght = 35

    days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    mon_to_sign = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

    total_sundial_type = ['italic', 'babilo', 'french']

    def __init__(self,
                lat,
                lon,
                h,
                alpha,
                beta,
                lamb,
                gamma,
                mon_to_plot,
                day_to_plot,
                year,
                start_hour,
                end_hour,
                max_dial_x,
                max_dial_y,
                sundial_type
                ):

        """
		Parameters needed to compute sundial.
		All parameters in the model must be
		upload here.
		
		Parameters:
		------------
		lat : float
			latitude
        lon : float
			longitude
        h : 
			gnomon length
        alpha : 

        beta :
        
		lamb :
        
		gamma : 
        
		mon_to_plot : specific string (see notes)
        
		day_to_plot : specific string (see notes)

        start_hour : int
        
        end_hour : int
		"""

        self.lat = lat
        self.lon = lon

        self.h = h

        self.alpha = alpha
        self.beta = beta
        self.lamb = lamb
        self.gamma = gamma

        self.mon_to_plot = mon_to_plot
        self.day_to_plot = day_to_plot

        self.year = year # just to put something

        self.start_hour = start_hour
        self.end_hour = end_hour

        self.max_dial_x = max_dial_x
        self.max_dial_y = max_dial_y

        self.sundial_type = sundial_type


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

        if(self.sundial_type == 'italic'):
            print("this kind of sundial has still to be implemented")
        elif(self.sundial_type == 'babilo'):
            print("this kind of sundial has still to be implemented")
        elif(self.sundial_type == 'french'):
            self._showSundialFrench()
        

    
    def _showSundialFrench(self):
    
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

            plt.scatter(x_dial, y_dial, label=self.mon_show[i])
        
        plt.legend()
        plt.axis("equal")
        plt.show()