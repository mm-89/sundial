import math as mt


def declination(year, day):
    """
    Ref. Mark_Z._Jacobson, Fundamentals of Atmospheric_Modeling ---- NO OTHER
    """

    conv_fact = mt.pi/180.

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
    lambda_ec = L_M + 1.915 * mt.sin(g_M * conv_fact) + \
    0.020 * mt.sin(2 * g_M * conv_fact)

    # solar declination angle
    delta = mt.asin(mt.sin(eps_ob * conv_fact) * mt.sin(lambda_ec * conv_fact))

    return delta

def get_xy_shade(year, day, lat, time_loc, h, alpha=0, beta=0, sigma=0, chi=0):
    """
    get shade of vertical gnomone

    alpha: for now the zenith angle of the piano
    beta: for now the angle respect the north of the piano
    sigma: for now the angle of gnomone respect the normal of the piano
    chi: the angle respect to the east of the piano
    """

    # change the time hour. The max is time_loc = 12
    H_a = ( 2 * mt.pi * time_loc) / 24. - mt.pi
    lat = lat * mt.pi / 180.

    alpha = alpha * mt.pi / 180.
    beta = beta * mt.pi / 180.

    sigma = sigma * mt.pi / 180.
    chi = chi * mt.pi / 180.

    #compute S in components
    Sx = - mt.cos(declination(year, day)) * mt.sin(H_a)

    Sy = mt.sin(declination(year, day)) * mt.cos(lat) - \
    mt.cos(declination(year, day)) * mt.sin(lat) * mt.cos(H_a)

    Sz = mt.cos(declination(year, day)) * mt.cos(lat) * mt.cos(H_a) + \
    mt.sin(declination(year, day)) * mt.sin(lat)

    # normal shade
    x_shade = - h * Sx / Sz
    y_shade = - h * Sy / Sz

    Sx_new = Sx * mt.cos(beta) - Sy * mt.sin(beta)

    Sy_new = (Sx * mt.sin(beta) + Sy * mt.cos(beta)) * mt.cos(alpha) - Sz * mt.sin(alpha)

    Sz_new = (Sx * mt.sin(beta) + Sy * mt.cos(beta)) * mt.sin(alpha) + Sz * mt.cos(alpha)

    x_shade_new = - h * mt.cos(sigma) * Sx_new / Sz_new + h * mt.sin(sigma) * mt.cos(sigma)
    y_shade_new = - h * mt.cos(sigma) * Sy_new / Sz_new + h * mt.sin(sigma) * mt.sin(sigma)

    # simply: only alpha
    Sx_pro = Sx
    Sy_pro = Sy * mt.cos(alpha) - Sz * mt.sin(alpha)
    Sz_pro = Sy * mt.sin(alpha) + Sz * mt.cos(alpha)

    x_shade_pro = - h * Sx_pro / Sz_pro
    y_shade_pro = - h * Sy_pro / Sz_pro
    

    return x_shade, y_shade, x_shade_new, y_shade_new
