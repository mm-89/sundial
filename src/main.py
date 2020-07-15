import sys
sys.path.insert(0, '../')

from namelist import *

from sundial import Sundial

# Parameters object with all parameters
# of the namelist

sundial = Sundial(lat,
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
				)
				
sundial.checkParams()
sundial.readParams()

sundial.showSundial()

# just to visualize right now ----------

"""
print(" {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}".format(sundial.lat_p,
sundial.lon_p,
sundial.h_p,
sundial.alpha_p,
sundial.beta_p,
sundial.lamb_p,
sundial.gamma_p,
sundial.mon_to_plot,
sundial.day_to_plot))
"""

#-------------------------------------
						


"""
import sundial
import read_param
import matplotlib.pyplot as plt
from math import *


h = 1

def plot_sundial(lon, lat, alpha, beta, lamb, gamma, mon, day, utc):

	time = [i for i in range(8,18)] #in in hours

	acc = 0
	new_day = []
	day_mon = []
	for i in range(len(mon)):
		if( mon[i] == 1 ):
			day_mon.append(i)
			acc += 1
			new_day.append(day[i])
	print(new_day)

	for i in range(acc):
		var_to_plot_x = []
		var_to_plot_y = []
		for j in time:
			var_x, var_y = \
	sundial.plain_shade_TOTAL(2019, new_day[i], j, lat, h, alpha, beta, lamb, gamma)
			if (var_x < 2*h and var_x > -2*h and var_y< 2*h and var_y > -2*h):
				plt.text(var_x, var_y, '%s' % j)
				var_to_plot_x.append(var_x)
				var_to_plot_y.append(var_y)
		print(var_to_plot_x, var_to_plot_y)
		plt.plot(var_to_plot_x, var_to_plot_y, label='%s' % mon_to_sign[day_mon[i]])
		plt.plot(var_to_plot_x, var_to_plot_y, '.')
		plt.legend()
		plt.xlim(xmin=-2*h,xmax=2*h)
		plt.ylim(ymin=-2*h,ymax=2*h)
		plt.axis('equal')

	return

"""
