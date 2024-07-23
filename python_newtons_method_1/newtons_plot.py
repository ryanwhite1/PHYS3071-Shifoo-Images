import numpy as np
import matplotlib.pyplot as plt

def newtons_method(function, derivative, init_guess):
    error = 10
    tol = 1e-6
    guess = init_guess
    while abs(error) > tol:
        new_guess = guess - function(guess) / derivative(guess)
        error = new_guess - guess
        guess = new_guess
    return guess

def plot_newtons(ax, function, derivative, init_guess, bound):
    x_arr = np.linspace(bound[0], bound[1], 100)
    ax.plot(x_arr, function(x_arr), c='k', alpha=0.8, label='Curve')
    ax.axhline(0, c='k')
    true_root = newtons_method(function, derivative, init_guess)
    ax.plot(true_root, 0, marker='x', mew=10, c='r', label='True Root')
    left, right = ax.get_xlim()
    bottom, top = ax.get_ylim()
    
    guess = init_guess
    
    tangents = ['First', 'Second', 'Third']
    
    for i in range(3):
        ax.plot([guess, guess], [0, function(guess)], c='k', ls='--', alpha=0.5)
        ax.plot(guess, function(guess), marker='o', c='k')
        ax.text(guess, -1, f'$x_{i}$')
        
        new_guess = guess - function(guess) / derivative(guess)
        gradient = function(guess) / (guess - new_guess)
        c = function(guess) - gradient * guess
        ax.plot(x_arr, gradient * x_arr + c, label=f'{tangents[i]} Tangent')
        guess = new_guess
        
    ax.set(xlim=(left, right), ylim=(bottom, top))


            
def func(x):
    return np.exp(x) - 4
def deriv(x):
    return np.exp(x)

# def func(x):
#     return x**2 - 3 * x
# def deriv(x):
#     return 2 * x - 3

fig, ax = plt.subplots()
plot_newtons(ax, func, deriv, 3.1, [1, 3.2])
ax.set(xlabel='$x$', ylabel='$y$')
ax.legend()

fig.savefig('Newtons_Rule.png', dpi=400, bbox_inches='tight')
# 


