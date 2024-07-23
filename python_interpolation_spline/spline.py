import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.linspace(0, 2*np.pi, 6)
fine_x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

spline = CubicSpline(x, y)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.plot(fine_x, spline(fine_x), label='Cubic Spline')
ax.plot(fine_x, np.sin(fine_x), label='True Function')
ax.legend()

fig.savefig('CubicSpline.png', dpi=400, bbox_inches='tight') 

fig, ax = plt.subplots()

ax.scatter(x, y)
ax.plot(fine_x, spline(fine_x), label='Cubic Spline')
ax.plot(fine_x, np.sin(fine_x), label='True Function')


derivative = spline.derivative(1) # first derivative
ax.plot(fine_x, np.cos(fine_x), label='True Derivative')
ax.plot(fine_x, derivative(fine_x), label='Spline Derivative')
ax.legend()
fig.savefig('CubicSplineDeriv.png', dpi=400, bbox_inches='tight')



question_x = np.linspace(-2, 2.5, 15)
question_y = np.sin(question_x**3)

np.savetxt('x_values.txt', question_x)
np.savetxt('y_values.txt', question_y)

# question_spl = CubicSpline(question_x, question_y)
# spl_deriv = question_spl.derivative(1)
# question_fine_x = np.linspace(-2, 2.5, 200)
# fig, axes = plt.subplots(nrows=2)
# axes[0].scatter(question_x, question_y)
# axes[0].plot(question_fine_x, np.sin(question_fine_x**3), label='True')
# axes[0].plot(question_fine_x, question_spl(question_fine_x), label='Spline')
# axes[1].plot(question_fine_x, np.sin(question_fine_x**3) - question_spl(question_fine_x), label="Error")
# # axes[1].plot(question_fine_x, spl_deriv(question_fine_x), label="Spline Derivative")
# axes[0].legend()
# axes[1].legend()

# fig.savefig("QuestionCorrect.png", dpi=400, bbox_inches='tight')
