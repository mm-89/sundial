import sys
from math import *

sys.path.insert(0, '../')

from namelist import *

# function definitions ---------------------------------------------

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
