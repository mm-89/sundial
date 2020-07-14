import math as mt

class ReadNamelist(object):
      
    def readParams(self):
        
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