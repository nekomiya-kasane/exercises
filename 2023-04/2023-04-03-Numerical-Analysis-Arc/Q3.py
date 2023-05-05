import numpy as np

def LU_decomposition(A,type=float):

    n = A.shape[0]

    L = np.eye(n, dtype=type)
    U = A.copy()
    for i in range(n):
        a = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = a
        U[i + 1:] -= a[:, np.newaxis] * U[i]
    return L, U

def LUSolve(A, b, type=float):
    L, U = LU_decomposition(A)

    # Ly = b
    n = L.shape[0]
    y = np.zeros_like(b, dtype=type)

    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # Ux = y
    n = U.shape[0]
    x = np.zeros_like(y, dtype=type)

    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x

# Question 1
A = np.array([
    [21.0, 67.0, 88.0, 73.0],
    [76.0, 63.0,  7.0, 20.0],
    [ 0.0, 85.0, 56.0, 54.0],
    [19.3, 43.0, 30.2, 29.4]
])
b = np.array([141.0, 109.0, 218.0, 93.7])

print("(a) Solution: ", LUSolve(A, b))

# Question 2
x = LUSolve(A, b, np.double)
r = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("(b) Residual: ", r)

# Question 3
z = LUSolve(A, r, np.double)
x = x + z
print("(c) Improved solution: ", x)

# Question 4
print("(d)")
r = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("Loop 1 residual: ", np.linalg.norm(r, ord=np.inf))
z = LUSolve(A, r, np.double)
x = x + z

r = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("Loop 2 residual: ", np.linalg.norm(r, ord=np.inf))
z = LUSolve(A, r, np.double)
x = x + z

r = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("Loop 3 residual: ", np.linalg.norm(r, ord=np.inf))
z = LUSolve(A, r, np.double)
x = x + z

r = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("Loop 4 residual: ", np.linalg.norm(r, ord=np.inf))
z = LUSolve(A, r, np.double)
x = x + z

rp = (b.astype(np.double) - A.astype(np.double) @ x).astype(float)
print("Loop 5 residual: ", np.linalg.norm(rp, ord=np.inf))

# in the 4th loop, the residue is the least.
print("Solution: ", x, " Residue", r)