class CheckNamelist(object):

    def checkParams(self):
       
        #first: check is variables are string

        #lat
        if not isinstance(self.lat, str):
            raise TypeError("LAT is not a string")

        #lon
        if not isinstance(self.lon, str):
            raise TypeError("LON is not a string")

        #angles
        if not isinstance(self.alpha, str):
            raise TypeError("ALPHA is not a string")
        if not isinstance(self.beta, str):
            raise TypeError("BETA is not a string")
        if not isinstance(self.lamb, str):
            raise TypeError("LAMBDA is not a string")
        if not isinstance(self.gamma, str):
            raise TypeError("GAMMA is not a string")

        #to_plot
        if not isinstance(self.mon_to_plot, str):
            raise TypeError("MONTH TO PLOT is not a string")
        if not isinstance(self.day_to_plot, str):
            raise TypeError("DAY TO PLOT is not a string")
        
        #second: check if the lenghts are correct

        #lat
        if not len(self.lat) in self.lat_lenght:
            raise IndexError("LAT is not of correct lenght")

        #lon
        if not len(self.lon) in self.lon_lenght:
            raise IndexError("LON is not of correct lenght")
    
        #angles
        if not len(self.alpha) in self.angles_lenght:
            raise IndexError("ALPHA is not of correct lenght")
        if not len(self.beta) in self.angles_lenght:
            raise IndexError("BETA is not of correct lenght")
        if not len(self.lamb) in self.angles_lenght:
            raise IndexError("LAMBDA is not of correct lenght")
        if not len(self.gamma) in self.angles_lenght:
            raise IndexError("GAMMA is not of correct lenght")

        #mon
        if not (len(self.mon_to_plot) == self.mon_list_lenght):
            raise IndexError("MONTH TO PLOT is not of correct lenght")

        #day
        if not (len(self.day_to_plot) == self.day_list_lenght):
            raise IndexError("DAY TO PLOT is not of correct lenght")
        

        #third: check the values inside
        
        #lat
        if len(self.lat) is 8:
            if not (self.lat[2] == '-' or self.lat[5] == '-'):
                raise ValueError("LAT is not correct setting")
        if len(self.lat) is 9:
            if not (self.lat[3] == '-' or self.lat[6] == '-'):
                raise ValueError("LAT is not correct setting")
            if not (self.lat[0] == '+' or self.lat[0] == '-'):
                raise ValueError("LAT can have a sign '+' or '-' at the beginning")

        #lon
        if len(self.lon) == 8:
            if not (self.lon[2] == '-' or self.lon[5] == '-'):
                raise ValueError("LON is not correct setting")
        if len(self.lon) == 9:
            if not (self.lon[3] == '-' or self.lon[6] == '-'):
                raise ValueError("LON is not correct setting")
            if not self.lon[0].isdigit():
                if not (self.lon[0] == '-' or self.lon[0] == '+') :
                    raise ValueError("LON can have a sign '+' or '-' at the beginning")
        if len(self.lon) == 10:
            if not (self.lon[4] == '-' or self.lon[7] == '-'):
                raise ValueError("LON is not correct setting")
            if not (self.lon[0] == '+' or self.lon[0] == '-'):
                raise ValueError("LON can have a sign '+' or '-' at the beginning")

        #mon
        if not all([item.isdigit() for item in self.mon_to_plot.split(' ')]):
            raise ValueError("MONTH TO PLOT  is not correct setting")

        #day
        if not all([item.isdigit() for item in self.day_to_plot.split(' ')]):
            raise ValueError("DAY TO PLOT is not correct setting")

        if not self.sundial_type in self.total_sundial_type:
            raise ValueError("Sundial type not recognize")