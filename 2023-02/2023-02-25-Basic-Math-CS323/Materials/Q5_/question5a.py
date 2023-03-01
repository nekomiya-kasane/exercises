import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=100):
    """
    Bisection method for finding the root of a nonlinear equation in one dimension.
    
    Arguments:
    f -- the function representing the equation
    a -- lower bound of the interval
    b -- upper bound of the interval
    tol -- tolerance for the root (default: 1e-6)
    max_iter -- maximum number of iterations (default: 100)
    
    Returns:
    x -- the root
    """
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        raise ValueError("The function does not have opposite signs at the interval endpoints.")
    for i in range(max_iter):
        x = (a + b) / 2
        fx = f(x)
        if fx == 0 or (b - a) / 2 < tol:
            return x
        if fx * fa > 0:
            a = x
            fa = fx
        else:
            b = x
    raise ValueError("The method did not converge.")

def newton(f, df, x0, tol=1e-6, max_iter=100):
    """
    Newton's method for finding the root of a nonlinear equation in one dimension.
    
    Arguments:
    f -- the function representing the equation
    df -- the derivative of the function
    x0 -- initial guess for the root
    tol -- tolerance for the root (default: 1e-6)
    max_iter -- maximum number of iterations (default: 100)
    
    Returns:
    x -- the root
    """
    for i in range(max_iter):
        fx = f(x0)
        if abs(fx) < tol:
            return x0
        x1 = x0 - fx / df(x0)
        x0 = x1
    raise ValueError("The method did not converge.")

def secant(f, x0, x1, tol=1e-6, max_iter=100):
    """
    Secant method for finding the root of a nonlinear equation in one dimension.
    
    Arguments:
    f -- the function representing the equation
    x0 -- first guess for the root
    x1 -- second guess for the root
    tol -- tolerance for the root (default: 1e-6)
    max_iter -- maximum number of iterations (default: 100)
    
    Returns:
    x -- the root
    """
    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if abs(fx1) < tol:
            return x1
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x0 = x1
        x1 = x2
    raise ValueError("The method did not converge.")

def f(x):
    return 3*x - 3*x**2 + 3*x - 1
