import sys
sys.path.insert(0, '../')

import namelist as nl
import sundial as sd

# Parameters object with all parameters
# of the namelist

sundial = sd.Sundial(nl.lat,
						nl.lon,
						nl.h,
						nl.alpha,
						nl.beta,
						nl.lamb,
						nl.gamma,
						nl.mon_to_plot,
						nl.day_to_plot
						)
sundial.checkParams()
sundial.readParams()

# just to visualize right now ----------

print(" {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}".format(sundial.lat,
sundial.lon,
sundial.h,
sundial.alpha,
sundial.beta,
sundial.lamb,
sundial.gamma,
sundial.mon_to_plot,
sundial.day_to_plot))

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
