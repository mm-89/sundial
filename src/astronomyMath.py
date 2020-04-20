import math as mt


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
    L_M = mt.radians(280.460) + mt.radians(0.9856474) * N_JD
	
    # mean anomaly of the Sun
    g_M = mt.radians(357.528) + mt.radians(0.9856003) * N_JD

    # obliquity of the ecliptic
    eps_ob = mt.radians(23.439) - mt.radians(0.0000004) * N_JD
	
    # ecliptic longitude of the Sun
    lambda_ec = L_M + mt.radians(1.915)*mt.sin(g_M) + \
    mt.radians(0.020)*mt.sin(g_M)

    # solar declination angle
    delta = mt.asin(mt.sin(eps_ob) * mt.sin(lambda_ec))

    return delta
