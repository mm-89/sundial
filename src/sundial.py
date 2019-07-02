from math import *


def declination(year, day):
    """
    Ref. Mark_Z._Jacobson, Fundamentals of Atmospheric_Modeling ---- NO OTHER
    """

    conv_fact = pi/180.

    # Julian day of the year
    D_J = day

    # number of leap days since or before the year 2000
    if(year>=2001):
        D_L = (year - 2001)/4
    else:
        D_L = (year - 2001)/4 - 1

    # number of days from the beginning of Julian year 2000
    N_JD = 364.5 + 365 * (year - 2001) + D_L + D_J
	
    # mean longitude of the Sun
    L_M = 280.460 + 0.9856474 * N_JD
	
    # mean anomaly of the Sun
    g_M = 357.528 + 0.9856003 * N_JD

    # obliquity of the ecliptic
    eps_ob = 23.439 - 0.0000004 * N_JD
	
    # ecliptic longitude of the Sun
    lambda_ec = L_M + 1.915 *sin(g_M * conv_fact) + \
    0.020 *sin(2 * g_M * conv_fact)

    # solar declination angle
    delta =asin(sin(eps_ob * conv_fact) * sin(lambda_ec * conv_fact))

    return delta

def get_s_component(year, day, lat, time_loc):
    """
    Only Sx, Sy, Sz components
    """ 
    # change the time hour. The max is time_loc = 12
    H_a = ( 2 *pi * time_loc) / 24. -pi

    #compute S in components
    Sx = -cos(declination(year, day)) * sin(H_a)
    Sy = sin(declination(year, day)) * cos(lat) - \
           cos(declination(year, day)) * sin(lat) *cos(H_a)
    Sz = cos(declination(year, day)) * cos(lat) * cos(H_a) + \
            sin(declination(year, day)) * sin(lat)
    
    return Sx, Sy, Sz

#-------------------------------------------------------

def plain_shade(year, day, time_loc, lat, h, alpha, beta):
    
    Sx = get_s_component(year, day, lat, time_loc)[0]
    Sy = get_s_component(year, day, lat, time_loc)[1]
    Sz = get_s_component(year, day, lat, time_loc)[2]

    Sx_up = Sx * cos(beta) - (-Sy * sin(alpha) + Sz * cos(alpha)) * sin(beta)
    Sy_up = Sy * cos(alpha) +  Sz * sin(alpha)
    Sz_up = Sx * sin(beta) + (-Sy * sin(alpha) + Sz * cos(alpha)) * cos(beta)

    x = - h * Sx_up / Sz_up
    y = - h * Sy_up / Sz_up

    return x, y

def plain_shade_TOTAL(year, day, time_loc, lat, h, alpha, beta, lamb, gamma):

    Sx_normal_palin_shade = plain_shade(year, day, time_loc, lat, h, alpha, beta)[0]
    Sy_normal_palin_shade = plain_shade(year, day, time_loc, lat, h, alpha, beta)[1]

    x_up = - h * sin(lamb) * sin(gamma) + Sx_normal_palin_shade * cos(lamb)
    y_up = - h * sin(lamb) * cos(gamma) + Sy_normal_palin_shade * cos(lamb)

    return x_up, y_up

def get_xy_shade(year, day, lat, time_loc, h, alpha, beta, lamb, gamma):
    """
    get shade of vertical gnomone

    alpha: for now the zenith angle of the piano
    beta: for now the angle respect the north of the piano
    sigma: for now the angle of gnomone respect the normal of the piano
    chi: the angle respect to the east of the piano
    """

    # change the time hour. The max is time_loc = 12
    H_a = ( 2 *pi * time_loc) / 24. -pi

    #compute S in components
    Sx = -cos(declination(year, day)) *sin(H_a)

    Sy =sin(declination(year, day)) *cos(lat) - \
   cos(declination(year, day)) *sin(lat) *cos(H_a)

    Sz =cos(declination(year, day)) *cos(lat) *cos(H_a) + \
   sin(declination(year, day)) *sin(lat)

    # normal shade
    x_shade = - h * Sx / Sz
    y_shade = - h * Sy / Sz

    Sx_new = Sx *cos(beta) - Sy *sin(beta)

    Sy_new = (Sx *sin(beta) + Sy *cos(beta)) *cos(alpha) - Sz *sin(alpha)

    Sz_new = (Sx *sin(beta) + Sy *cos(beta)) *sin(alpha) + Sz *cos(alpha)

    x_shade_new = - h *cos(lamb) * Sx_new / Sz_new + h *sin(lamb) *cos(lamb)
    y_shade_new = - h *cos(lamb) * Sy_new / Sz_new + h *sin(lamb) *sin(lamb)

    # simply: only alpha
    Sx_pro = Sx
    Sy_pro = Sy *cos(alpha) - Sz *sin(alpha)
    Sz_pro = Sy *sin(alpha) + Sz *cos(alpha)

    x_shade_pro = - h * Sx_pro / Sz_pro
    y_shade_pro = - h * Sy_pro / Sz_pro
    

    return x_shade_new, y_shade_new

def time_eq(year, day):
    """
    equation of time (to rewrite), from wikipedia (for now).
    """
    conv_fact = pi/180.

    # Julian day of the year
    D_J = day

    # equation of time (E in minute) from wiki
    eqtime = -9.87 * sin(2 * 2 * pi/365. * (D_J - 81)) + \
    7.67 * sin(2 * pi/365. *(D_J -1))
    
    return eqtime
