
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

#-----------------------------------------------


class Parameters(object):

    lat_lenght = [8, 9]
    lon_lenght = [8, 9, 10]

    angles_lenght = [2, 3]

    mon_list_lenght = 23
    day_list_lenght = 35

    days_in_a_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    mon_to_sign = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic']

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
                max_dial_y
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