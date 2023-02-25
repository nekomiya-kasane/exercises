# f(x) = 1 + x(2 + x(3 + x(4 + x(5 + x(6 + x(7 + 8x))))))
arr = [1,2,3,4,5,6,7,8]

t0 = 2 # at t0=2

def eval(a: list[float], t0: float) -> tuple[float, float]:
    if len(a) == 1:
        return a[0], 0
    elif not len(a):
        return 0, 0
    
    p = a[-1]
    q = 0

    for i in range(len(a) - 2, -1, -1):
        q = p + t0 * q
        p = a[i] + t0 * p

    return p, q

p, q = eval(arr, t0)
print("Value: ", p) 
print("Derivative: ", q)

# f(x) = 2 + x(-2 + x(3 + x(-4 + x(5 + x(-6 + x(7 - 8x))))))
arr = [2,-2,3,-4,5,-6,7,-8]

t0 = 3 # at t0=3

p, q = eval(arr, t0)
print("Value: ", p)
print("Derivative: ", q)