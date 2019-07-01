import sundial
import read_param
import matplotlib.pyplot as plt
from math import *


h = 1


def plot_sundial(lon, lat, alpha, beta, lamb, gamma, mon, day, utc):
	"""
	somethings
	"""
	time = [i for i in range(6,18)] #in in hours

	acc = 0
	new_day = []
	for i in range(len(mon)):
		if( mon[i] == 1 ):
			acc += 1
			new_day.append(day[i])
	print(new_day)

	for i in range(acc):
		var_to_plot_x = []
		var_to_plot_y = []
		for j in time:
			var_x, var_y = sundial.get_xy_shade(2019, new_day[i], lat, j, h, alpha, beta, lamb, gamma)
			if (var_x < 2*h and var_x > -2*h and var_y< 2*h and var_y > -2*h):
				plt.text(var_x, var_y, '%s' % j)
				var_to_plot_x.append(var_x)
				var_to_plot_y.append(var_y)
		print(var_to_plot_x, var_to_plot_y)
		plt.plot(var_to_plot_x, var_to_plot_y)
		plt.plot(var_to_plot_x, var_to_plot_y, '.')
		plt.xlim(xmin=-2*h,xmax=2*h)
		plt.ylim(ymin=-2*h,ymax=2*h)

	return
