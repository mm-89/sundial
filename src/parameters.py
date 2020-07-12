class Parameters:

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
