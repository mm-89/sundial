from math import cos, sin, radians, pi


def solar_declination_angle(year, day):
    """
    Ref. Mark_Z._Jacobson, Fundamentals of Atmospheric Modeling
    Second edition, pg. 318
    """

    # day is the Julian day of the year, so
    # 1 is the 1st of January, 365 is the 
    # 31th of December
 
    # number of leap days since or before the year 2000
    if(year>=2001):
        D_L = (year - 2001)/4
    else:
        D_L = (year - 2001)/4 - 1

    # number of days from the beginning of Julian year 2000
    N_JD = 364.5 + 365 * (year - 2001) + D_L + day
	
    # mean longitude of the Sun
    L_M = radians(280.460) + radians(0.9856474) * N_JD
	
    # mean anomaly of the Sun
    g_M = radians(357.528) + radians(0.9856003) * N_JD

    # obliquity of the ecliptic
    eps_ob = radians(23.439) - radians(0.0000004) * N_JD
	
    # ecliptic longitude of the Sun
    lambda_ec = L_M + radians(1.915)*sin(g_M) + \
        radians(0.020)*sin(g_M)

    # solar declination angle
    delta = asin(mt.sin(eps_ob) * sin(lambda_ec))

    return delta

def equation_of_time(year, day):
    """
    equation of time, from wikipedia (for now).
    """
    # equation of time (E in minute)
    eq_of_time = -9.87 * sin(2 * 2 * pi/365. * (day - 81)) + \
    7.67 * sin(2 * pi/365. *(day -1))

    return eq_of_time

