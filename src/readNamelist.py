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

class ReadNamelist:

    days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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
        alpha_new = mt.radians(float(self.alpha))
        beta_new = mt.radians(float(self.beta))
        lamb_new = mt.radians(float(self.lamb))
        gamma_new = mt.radians(float(self.gamma))

        #days and months
        mon_new = [float(i) for i in self.mon_to_plot.split(' ')]
        day_new = [float(i) for i in self.day_to_plot.split(' ')]
        
        #day cumulative for each mon
        #from 0 to 334
        cum_days = [sum(self.days_in_a_month[:i]) for i in range(len(self.days_in_a_month))]
        
        #sum current day_to_plot to have the shift in right days
        cum_days_to_plot = [cum_days[j] + day_new[j] for j, i in enumerate(mon_new) if i != 0]


if __name__ == "__main__":
    current_read = ReadNamelist(nl.lat,
                                nl.lon,
                                nl.h,
                                nl.alpha,
                                nl.beta,
                                nl.lamb,
                                nl.gamma,
                                nl.mon_to_plot,
                                nl.day_to_plot
                                )
    current_read.general_read()

