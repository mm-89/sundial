import sys
import math as mt

sys.path.insert(0, '../')

import namelist import nl

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
# 2- if the value is correct

class CheckNamelist:

    geo_lenght = 9

    angles_lengh = 3

    mon_list_lenght = 22
    day_list_lenght = 34
    

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
        
        #to give at the end
        self.verify_string = True
        self.verify_lenght = True
        self.verify_value = True


    def general_check(self):

        # first: check if every one is a string

        #...

        # second: check the leghts

        #lat
        if(len(self.lat) != geo_lenght): self.verify_lenght = False

        #lon
        if(len(self.lon) != geo_lenght): self.verify_lenght = False
    
        #angles
        if(len(self.alpha) != angles_length): self.verify_lenght = False
        if(len(self.beta) != angles_length): self.verify_lenght = False
        if(len(self.lamb) != angles_length): self.verify_lenght = False
        if(len(self.gamma) != angles_length): self.verify_lenght = False

        #mon
        if(len(self.mon_to_plot) != mon_list_lenght): self.verify_lenght = False

        #day
        if(len(self.day_to_plot) != day_list_lenght): self.verify_lenght = False
        

        # third: check the values

        if(self.verify_lenght):

            #lat
            if(not self.lat[0] == '+' or not self.lat[0] == '-'):
                self.verify_value = False
            if(not self.lat[3] == '-' or not self.lat[6] == '-'):
                self.verify_value = False

            #lon
            if(not self.lon[0] == '+' or not self.lon[0] == '-'):
                self.verify_value = False
            if(not self.lon[3] == '-' or not self.lon[6] == '-'):
                self.verify_value = False
            
            #lat
            try:
                self.lat_new = float(self.lat[1:3]) + \
                                float(self.lat[4:6])/60. + \
                                float(self.lat[7:9])/3600.
            except:
                self.verify_value = False

            #lon
            try:
                self.lon_new = float(long_val[0:2]) + \
                                float(long_val[3:5])/60. + \
                                float(long_val[6:8])/3600.
            except:
                self.verify_value = False

            #angles
            try:
                self.alpha_new = float(self.alpha)*mt.pi/180.
                self.beta_new = float(self.beta)*mt.pi/180.
                self.lamb_new = float(self.lamb)*mt.pi/180.
                self.gamma_new = float(self.gamma)*mt.pi/180.
            except:
                self.verify_value = False







def trans_degree_decimal_lon(long_val):
    """
    Some definition
    """
    new_val = float(long_val[0:2]) + float(long_val[3:5]) / 60. +\
            float(long_val[6:8]) / 3600.
    return new_val

def trans_degree_decimal_lat(long_val):
    """
    Some definition
    """
    new_val = float(long_val[1:3]) + float(long_val[4:6]) / 60. +\
            float(long_val[7:9]) / 3600.
    if(long_val[0]=='-'):
        new_val = - new_val
        
    return new_val


def trans_degree_to_radiant(angle):
    """
    Some definition
    """
    new_angle = angle * pi / 180.
	
    return new_angle

def check_type_and_len_coordinates_lon(param):
    """
    note: 
    		true = ok
    		false = there's a problema
    """
    verify = True

    if( not type(param) is str):
        verify = False
    if( not len(param) is 8):
        verify = False

    return verify

def check_type_and_len_coordinates_lat(param):
    """
    note: 
	true = ok
	false = there's a problema
    """

    verify = True

    if( not type(param) is str):
        verify = False
    if( not len(param) is 9):
        verify = False
    return verify

def check_dimension_coordinates_lon(long_val):
    """
    note:
    		true: ok
    		false: there's a problem
    """
    verify = True

    degree = float(long_val[0:2])
    minute = float(long_val[3:5]) 
    second = float(long_val[6:8])
    if(degree < 0. or degree > 360.):
        verify = False
    if(minute < 0. or minute > 60.):
        verify = False
    if(second < 0. or second > 60.):
        verify = False

    return verify

def check_dimension_coordinates_lat(long_val):
    """
    note:
                true: ok
                false: there's a problem
    """
    verify = True

    degree = float(long_val[1:3])
    minute = float(long_val[4:6])
    second = float(long_val[7:9])

    if(degree < 0. or degree > 90.):
        verify = False
    if(minute < 0. or minute > 60.):
        verify = False
    if(second < 0. or second > 60.):
        verify = False

    return verify

def check_angles_dimension(angles):
    """
    note:
                true: ok
                false: there's a problem
    """
    verify = True
    if( not len(angles) is 2):
        verify = False
    return verify


def check_angles(angles):
    """
    note:
                true: ok
                false: there's a problem
    """
    verify = True
    val = float(angles)

    if(degree < 0. or degree > 90.):
        verify = False
    
    return verify

def check_monlist_dimension(monlist):
    """
    note:
                true: ok
                false: there's a problem
    """
    verify = True
    if( not len(monlist) is 23):
        verify = False
    return verify

def check_daylist_dimension(daylist):
    """
    note:
                true: ok
                false: there's a problem
    """
    verify = True
    if( not len(daylist) is 35):
        verify = False
    return verify

def check_mon_list_type(monlist):
    """
    note:
                true: ok
                false: there's a problem
    """ 
    verify = True
    val_to_check = ['1','0',' ']
    for i in monlist:
        if ( not i in val_to_check):
            verify = False
    return verify

def check_day_list_type(daylist):
    """
    note:
            true: ok
            false: there's a problem
            TO CONTINUE
    """
    verify = True
    return verify

def transform_month(monlist):
    """
    somethings
    """
    days_vector = []
    for i in range(0,len(monlist),2):
        days_vector.append(float(monlist[i]))

    return days_vector

def transform_days(monlist):
    """
    sometinghs
    """
    mon_vector = []
    for i in range(0,len(monlist),3):
        mon_vector.append(float(monlist[i:i+2]))

    day_for_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    cum_mon = []
    cum_mon.append(float(mon_vector[0]))
    acc = day_for_month[0]
    for i in range(11):
        acc += mon_vector[i+1]
        cum_mon.append(float(acc))
        acc -= mon_vector[i+1]
        acc += day_for_month[i+1]
    return cum_mon

def transform_UTC(utc):
	"""
	something
	"""
	if(utc[0] == '0'):
		val = float(utc[1]) * 15.
	else:
		val = float(utc) * 15.
	return val

