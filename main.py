import sundial
import matplotlib.pyplot as plt
import math as mt

a = 1
year = 2018
day = 30
lat = 30
h = 1

time = [i for i in range(9,16)] #in in hours

var_x = []
var_y = []

var_x_new = []
var_y_new = []

for el in time:
	var_x.append(sundial.get_xy_shade(year, day, lat, el, h, 0, 0)[0])
	var_y.append(sundial.get_xy_shade(year, day, lat, el, h, 0, 0)[1])
	var_x_new.append(sundial.get_xy_shade(year, day, lat, el, h, -40, 10, 30, 10)[2])
	var_y_new.append(sundial.get_xy_shade(year, day, lat, el, h, -40, 10, 30, 10)[3])

plt.subplot(121)
plt.plot(var_x, var_y)
plt.xlim(xmin=-2,xmax=2)
plt.ylim(ymin=0,ymax=2)

plt.subplot(122)
plt.plot(var_x_new, var_y_new)
plt.xlim(xmin=-2,xmax=2)
plt.ylim(ymin=0,ymax=2)

plt.show()
