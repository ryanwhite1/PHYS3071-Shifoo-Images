def truncated_gaussian(amplitude, mu, sigma, x):
    if x < (mu - 3 * sigma) or x > (mu + 3 * sigma):
        return 0
    else:
        return amplitude * np.e**(-0.5 * ((x - mu)/sigma)**2)

# get the user to input the cartesian coordinates
x_coord = float(input("Enter the x axis coordinate: "))
y_coord = float(input("Enter the y axis coordinate: "))
z_coord = float(input("Enter the z axis coordinate: "))

# import numpy and convert to spherical coordinates below:
import numpy as np
radius = np.sqrt(x_coord**2 + y_coord**2 + z_coord**2)
theta = np.arccos(z_coord / radius)
phi = np.sign(y_coord) * np.arccos(x_coord / np.sqrt(x_coord**2 + y_coord**2))

# and now convert back to cartesian coordinates to make sure we did the math correctly!
x_again = radius * np.sin(theta) * np.cos(phi)
y_again = radius * np.sin(theta) * np.sin(phi)
z_again = radius * np.cos(theta)