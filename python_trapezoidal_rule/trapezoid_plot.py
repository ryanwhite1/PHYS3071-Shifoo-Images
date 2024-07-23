import numpy as np
import matplotlib.pyplot as plt

def plot_trapezoidal(ax, xdata, ydata):
    coloured = 0
    
    ax.axhline(0, c='k', alpha=0.5)
    ax.plot(xdata, ydata, c='k', alpha=0.5, label='Trapezoids')
    
    for i in range(len(ydata)):
        ax.plot([xdata[i], xdata[i]], [0, ydata[i]], c='k', alpha=0.5)
        
        if i > 0:
            colour = 'tab:blue' if i%2 == 0 else 'tab:orange'
            ax.fill_between(xdata[i-1:i+1], ydata[i-1:i+1], color=colour, alpha=0.6)

def trapezoidal_rule(xdata, ydata):
    Sum = 0
    for i in range(1, len(xdata)):
        Sum += (ydata[i - 1] + ydata[i]) * (xdata[i] - xdata[i - 1]) / 2
    return Sum
            
def func(x):
    return 2 + x**2 - 1/12 * x**3

xdata = np.linspace(-2, 10, 6)
ydata = func(xdata)

fine_x = np.linspace(min(xdata), max(xdata), 100)
fine_y = func(fine_x)

fig, ax = plt.subplots()
plot_trapezoidal(ax, xdata, ydata)
ax.plot(fine_x, fine_y, c='tab:red', lw=2, label='True Curve')
ax.set(xlabel='$x$', ylabel='$y$')
ax.legend()

fig.savefig('Trapezoidal_Rule.png', dpi=400, bbox_inches='tight')



# coarse_integral = trapezoidal_rule(xdata, ydata)
# fine_integral = trapezoidal_rule(fine_x, fine_y)
# n = int(1e5)
# finest_integral = trapezoidal_rule(np.linspace(min(xdata), max(xdata), n), func(np.linspace(min(xdata), max(xdata), n)))

def problem_func(x):
    return np.sqrt(np.sin(x / np.pi)**2) + np.exp(x / 20) - 1.5
n = 23
problem_x = np.sort(np.random.uniform(-3, 20, n))
problem_y = problem_func(problem_x)

np.savetxt('x_values.txt', problem_x)
np.savetxt('y_values.txt', problem_y)

fig, ax = plt.subplots()
ax.plot(problem_x, problem_y)
plot_trapezoidal(ax, problem_x, problem_y)



