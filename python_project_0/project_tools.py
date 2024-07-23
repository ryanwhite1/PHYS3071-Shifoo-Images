import numpy as np

def newtons_method(func, func_dash, init_guess, tolerance):
    guess = init_guess
    iters = int(1e3)
    for i in range(iters):
        new_guess = guess - func(guess) / func_dash(guess)
        if abs(guess - new_guess) < tolerance:
            break
        guess = new_guess
        if i == iters - 1:
            guess = np.nan
    return guess

def trapezoidal_rule(xdata, ydata):
    cumsum = 0
    for i in range(1, len(xdata)):
        cumsum += (ydata[i - 1] + ydata[i]) * (xdata[i] - xdata[i - 1]) / 2
    return cumsum
