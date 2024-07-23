import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import project_tools as proj

def func(x):
    return np.cos(np.exp(x) / x) * np.exp(-(x - 2.5)**2)

x = np.linspace(0.001, 5, 40)
y = func(x)
# over this domain, we should have roots at [0.178, 0.296, 2.44, 3.23, 3.70, 4.04, 4.31, 4.53, 4.71, 4.86]

np.savetxt('x_values.txt', x)
np.savetxt('y_values.txt', y)

spline = CubicSpline(x, y)
fine_x = np.linspace(0.001, 5, 1000)
fine_y = spline(fine_x)

fig, axes = plt.subplots(nrows=2)
axes[0].scatter(x, y, label='Data')
axes[0].plot(fine_x, func(fine_x), label='True')
axes[0].plot(fine_x, fine_y, label='Spline')
axes[0].axhline(0, ls='--', c='k')

axes[1].plot(fine_x, fine_y**2, label=r'$|f(x, y)|^2$')
print("Total Area = ", proj.trapezoidal_rule(fine_x, fine_y**2))

for ax in axes:
    ax.legend()

fig.savefig("CorrectPlot.png", dpi=400, bbox_inches='tight')




