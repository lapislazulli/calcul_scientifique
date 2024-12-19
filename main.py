import numpy
import matplotlib.pyplot as plt
#from config_file import * if we write lenght and height instead of actual numbers or if we want to have it else where

def f(x):
    return x**2 - 8 * numpy.log(x)

def g(x):
    return x**3 - 3 

def solve_equation(f, left, right, precision=10**(-3)):
    while right - left >= precision:
        middle = (right + left) / 2

        if f(middle) == 0:
            return middle
        elif f(left) * f(middle) < 0:
            right = middle
        else:  # This means f(right) * f(middle) < 0
            left = middle

    return (right + left) / 2

def plot_function(f, start, end, step=0.1):
    x = numpy.arange(start, end, step)
    y = f(x)
    
    plt.figure(figsize=(15, 6))
    plt.plot(x, y, "*")
    plt.axhline(0, color='blue', linewidth=0.8, linestyle='--')  # Add x-axis for reference
    plt.title("Plot of the Function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(False)
    plt.show()

if __name__ == "__main__":
    # Plotting the function f
    plot_function(f, start=0.1, end=5, step=0.1)

    # Solving the equation for g
    middle = solve_equation(g, left=1, right=2)
    print("Root approximation for g(x):", middle)
    print("Function value at root:", g(middle))