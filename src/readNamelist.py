import math as mt

class ReadNamelist(object):
      
    def readParams(self):
        
        #lat
        self.lat_p = mt.radians(float(self.lat[:-6]) + \
                    float(self.lat[-5:-3])/60. + \
                    float(self.lat[-2:])/3600.)
        
        #lon
        self.lon_p = mt.radians(float(self.lon[:-6]) + \
                    float(self.lon[-5:-3])/60. + \
                    float(self.lon[-2:])/3600.)

        #angles
        self.alpha_p = mt.radians(float(self.alpha))
        self.beta_p = mt.radians(float(self.beta))
        self.lamb_p = mt.radians(float(self.lamb))
        self.gamma_p = mt.radians(float(self.gamma))

        self.h_p = float(self.h)

        #days and months
        self.mon_p = [float(i) for i in self.mon_to_plot.split(' ')]
        self.day_p = [float(i) for i in self.day_to_plot.split(' ')]
        
        self.mon_show = [self.mon_to_sign[i] for i in range(len(self.mon_to_sign)) if self.mon_p[i]==1]
        
        #day cumulative for each mon
        #from 0 to 334
        self.cum_days = [sum(self.days_in_a_month[:i]) for i in range(len(self.days_in_a_month))]
        
        #sum current day_to_plot to have the shift in right days
        #vector of days during a year to be plotted
        self.cum_days_to_plot = [self.cum_days[j] + self.day_p[j] for j, i in enumerate(self.mon_p) if i != 0]

        self.hours_per_day = [i for i in range(self.start_hour, self.end_hour + 1)]

        self.max_dial_x = float(self.max_dial_x)
        self.max_dial_y = float(self.max_dial_y)