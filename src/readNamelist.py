import sys
import math as mt

sys.path.insert(0, '../')

import namelist as nl

#------------------------------------------------

#current namelist parameters:
# 1- lat
# 2- lon
# 3- h

# 4- alpha
# 5- beta
# 6- lamb
# 7- gamma

# 8- mon_to_plot
# 9- day_to_plot

#-----------------------------------------------

#two points to check:

# 1- if the lengh is correct
# 2- if the value is correct (e.g. a string)

class ReadNamelist:

    def __init__(self,
                lat,
                lon,
                h,
                alpha,
                beta,
                lamb,
                gamma,
                mon_to_plot,
                day_to_plot
                ):

        self.lat = lat
        self.lon = lon

        self.h = h

        self.alpha = alpha
        self.beta = beta
        self.lamb = lamb
        self.gamma = gamma

        self.mon_to_plot = mon_to_plot
        self.day_to_plot = day_to_plot

        
    def general_read(self):
        
        #lat
        lat_new = float(self.lat[:-6]) + \
                    float(self.lat[-5:-3])/60. + \
                    float(self.lat[-2:])/3600.
        
        #lon
        lon_new = float(self.lon[:-6]) + \
                    float(self.lon[-5:-3])/60. + \
                    float(self.lon[-2:])/3600.

        #angles
        alpha_new = mt.radians(float(alpha))
        beta_new = mt.radians(float(beta))
        lamb_new = mt.radians(float(lamb))
        gamma_new = mt.radians(float(gamma))

