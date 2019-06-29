import sys

sys.path.insert(0, './src/')

import read_param as rp
import main as mn
import matplotlib.pyplot as plt

lon, lat, alpha, beta, lamb, gamma,\
mon, day, utc = rp.program_check()

mn.plot_sundial(lon, lat, alpha, beta, lamb, gamma, mon, day, utc)
plt.show()
