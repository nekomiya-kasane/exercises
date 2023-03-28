import numpy as np
from scipy.integrate import odeint, solve_ivp
import matplotlib.pyplot as plt
import matplotlib.animation as anime
import matplotlib.animation as animation

import os, sys

SUN, MERCURY, VENUS, EARTH, MARS, JUPITER, SATURN = 0, 1, 2, 3, 4, 5, 6
TS, XS, YS, ZS, XRANGE, YRANGE, ZRANGE = 0, 1, 2, 3, 4, 5, 6

atol = 1e-6
rtol = 1e-8

fig_index = 0
frames_per_call = 25

# plot colors
colors = ["green", "red", "blue", "orange", "purple", "pink", "yellow"]

#################################################################################################

au2m = 1.495978707e11
m2au = 1 / au2m 

yr2sec = 365 * 24 * 60 * 60
sec2yr = 1 / yr2sec

names = ["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupyter", "Saturn"]

N = len(names)
N3 = N * 3

# kg
_masses = np.array([1.98844e30, 3.30104e23, 4.86732e24, 5.97219e24, 6.41693e23, 1.89813e27, 5.68319e26]) 
masses = _masses / _masses[EARTH]

# AU
majors = np.array([0, 0.387098261, 0.723333771, 1, 1.523706365, 5.20287342, 9.536651047])
_majors = au2m * majors

eccentricities = np.array([0, 0.20563593, 0.00677672, 0.01671123, 0.0933941, 0.04838624, 0.05386179])

# year
periods = np.array([0, 0.2408425, 0.6151866, 1.0, 1.8808149, 11.862409, 29.446986])
_periods = yr2sec * periods

perihelion = majors * (1 - eccentricities)
_perihelion = au2m * perihelion

total_mass = np.sum(masses)

_G = 6.6743015e-11
G = 4 * np.pi ** 2 / total_mass

velocity = np.sqrt(np.divide(
    G * total_mass * (1 + eccentricities) / (1 - eccentricities), 
    majors, 
    out=np.zeros_like(majors), 
    where=majors!=0
)) # in AU / yr

inclination = np.array([0, 7.01, 3.39, 0, 1.85, 1.31, 2.49]) / 180 * np.pi # 0.77 1.77 17.14

arguments = {
    "Mass": masses,
    "Major": majors,
    "Eccentricity": eccentricities,
    "Period": periods,
    "Perihelion": perihelion,
    "Inclination": inclination,

    "Include": [],
    "Method": "Newton"
}

init_position = perihelion * np.concatenate([np.cos(inclination), np.zeros(N), np.sin(inclination)]).reshape(3, N)
init_position[0, SUN] = init_position[1, SUN] = init_position[2, SUN]
init_position = init_position.T

init_velocity = np.concatenate([np.zeros(N), velocity, np.zeros(N)]).reshape(3, N).T


###################################################################################################

def accelaration_newton(pos_this: np.ndarray, pos_that: np.ndarray, mass_that: float, G: float):
    r = pos_that - pos_this   # type: ignore
    res = G * mass_that * r / np.linalg.norm(r) ** 3
    return res

def advance_newton(t: float, state: np.ndarray, args: dict):
    # x * N3 + v * N3
    pos = state[:N3].reshape(N, 3)
    vel = state[N3:].reshape(N, 3)

    mass, major, ecc, period, peri, incl, inc, _ = args.values()
    if not len(inc):
        inc = list(range(N))
    for i in range(N):
        if i not in inc:
            vel[i] = np.zeros(3)

    step_pos = vel.copy()
    step_vec = np.zeros((N, 3))

    for i in inc: # for the i-th planet
        acc = np.zeros(3)
        for j in inc: 
            if j == i: 
                continue
            acc += accelaration_newton(pos[i, :], pos[j, :], mass[j], G)
        step_vec[i, :] = acc

    res = np.concatenate((step_pos.flatten(), step_vec.flatten()))
    return res

def adapter(t: float, state: np.ndarray, args: dict, method: str):
    return advance_newton(t, state, args)

def get_components(solution):
    ts = solution.t
    ys = solution.y.T

    poses = np.array([x[:N3].reshape(N, 3) for x in ys])

    xs = np.array([poses[:, i, 0] for i in range(N)]).T
    ys = np.array([poses[:, i, 1] for i in range(N)]).T
    zs = np.array([poses[:, i, 2] for i in range(N)]).T

    xrange = (min(xs.flatten()) - 1, max(xs.flatten()) + 1)
    yrange = (min(ys.flatten()) - 1, max(ys.flatten()) + 1)
    zrange = (min(zs.flatten()) - 1, max(zs.flatten()) + 1)

    return (ts, xs, ys, zs, xrange, yrange, zrange)

def draw_orbits(components, incs=[]):
    if not len(incs):
        incs = list(range(N))

    xs_copy = components[XS][:, incs].copy()
    ys_copy = components[YS][:, incs].copy()
    zs_copy = components[ZS][:, incs].copy()

    plt.rcParams["animation.html"] = "jshtml"
    plt.rcParams['figure.dpi'] = 80  
    plt.ioff()

    fig = plt.figure(fig_index)
    ax = fig.axes
    ax = plt.axes(projection='3d')

    plt.xlabel("X")
    plt.ylabel("Y")
    ax.set_zlabel("Z") # type: ignore

    plt.legend(["Curve", "X, Y", "X, Z", "Y, Z"])

    plt.xlim(components[XRANGE][0], components[XRANGE][1])
    plt.ylim(components[YRANGE][0], components[YRANGE][1])
    ax.set_zlim(components[ZRANGE][0], components[ZRANGE][1])  # type: ignore

    # def update_lines(num):
    #     for i in range(len(xs_copy[0, :])):
    #         ax.plot3D(
    #             xs_copy[:num, i], 
    #             ys_copy[:num, i], 
    #             zs_copy[:num, i], 
    #             color=colors[i])  # type: ignore

    # animation.FuncAnimation(fig, update_lines, np.arange(0, len(xs_copy[:, 0])), fargs=(),
    #                                interval=50, blit=False)
    
    for i in range(len(xs_copy[0, :])):
            ax.plot3D(
                xs_copy[:, i], 
                ys_copy[:, i], 
                zs_copy[:, i], 
                color=colors[i])  # type: ignore

    plt.show()

def draw_orbits_anime(ts, xs, ys, zs, xlim, ylim, zlim):
    pass

class Solution:
    def __init__(self, t, y, err):
        self.t = t
        self.y = y
        self.err = err
    

def solve(f, tspan, y0, N):
    h = (tspan[1] - tspan[0]) / N
    ts, sol = [tspan[0]], [y0]
    err = []
    while ts[-1] < tspan[1]:
        y_last = sol[-1].copy()
        
        t = ts[-1]
        k1 = f(t, y_last)
        k2 = f(t + h / 2, y_last + k1 * h / 2)
        k3 = f(t + h / 2, y_last + k2 * h / 2)
        k4 = f(t + h, y_last + k3 * h)
        y_new = y_last + (k1 + 2 * k2 + 2 * k3 + k4) * h / 6

        k1 = f(t, y_last)
        k2 = f(t + h, y_last + k1 * h)
        k3 = f(t + h, y_last + k2 * h)
        k4 = f(t + 2 * h, y_last + k3 * 2 * h)
        y_new_2 = y_last + (k1 + 2 * k2 + 2 * k3 + k4) * h / 3
        sol.append(y_new)

        ts.append(t + h)
        err.append(max(abs(y_new_2 - y_last)))
    
    return Solution(np.array(ts), np.array(sol).T, np.array(err))


# def solve_dorpi(f, tspan, y0, tol, max_iter):
#     cur_step = tol ** 0.2;
#     min_step = (tspan[1] - tspan[0]) / 1000.0;
#     max_step = (tspan[1] - tspan[0]) / 10.0;
#     default_step = (tspan[1] - tspan[0]) / 100.0;

#     a21 = 0.2
#     a31, a32 = 3 / 40., 9 / 40.
#     a41, a42, a43 = 44 / 45., -56 / 15., 32 / 9.
#     a51, a52, a53, a54 = 19372 / 6561., -25360 / 2187., 32 / 9., -212.0 / 729.0
#     a61, a62, a63, a64, a65 = 9017 / 3168., -355 / 33., 46732 / 5247., 49 / 176., -5103 / 18656.
#     a71, a72, a73, a74, a75, a76 = 35 / 384., 0.0, 500 / 1113., 125 / 192., -2187 / 6784., 11 / 84.

#     e1, e2, e3, e4, e5, e6 = 71 / 57600., -1 / 40., -71 / 16695., 71 / 1920., -17253 / 339200., 22 / 525.

#     ts, sol = [tspan[0]], [y0]
#     i = 0
#     while ts[-1] < tspan[1] and i < max_iter:
#         y_last = sol[-1].copy()
        
#         t = ts[-1]
#         k1 = f(t, y_last)
#         k2 = f(t, y_last + cur_step * a21 * k1)
#         k3 = f(t, y_last + cur_step * (a31 * k1 + a32 * k2))
#         k4 = f(t, y_last + cur_step * (a41 * k1 + a42 * k2 + a43 * k3))
#         k5 = f(t, y_last + cur_step * (a51 * k1 + a52 * k2 + a53 * k3 + a54 * k4))
#         k6 = f(t, y_last + cur_step * (a61 * k1 + a62 * k2 + a63 * k3 + a64 * k4 + a65 * k5))
#         k7 = y_last + cur_step * (a71 * k1 + a72 * k2 + a73 * k3 + a74 * k4 + a75 * k5 + a76 * k6)
#         k2 = f(t, k7)
        
#         error = cur_step * max(abs(e1 * k1 + e2 * k2 + e3 * k3 + e4 * k4 + e5 * k5 + e6 * k6))
#         if error < tol:
#             t += cur_step
#             if cur_step < min_step or cur_step > max_step:
#                 cur_step = default_step
#             k1 = k2
#             y_new = k7
#             sol.append(y_new)
#             ts.append(t)

#         koef = pow(tol / (2.0 * error), 0.2)
#         mx = max(koef, 0.3)
#         cur_step *= 0.9 * min(mx, 2)

#         if cur_step >= tspan[1]:
#             break
#         elif cur_step >= tspan[1] - t:
#             cur_step = tspan[1] - t

#         i += 1
    
#     return Solution(np.array(ts), np.array(sol).T)


###################################################################################################

t_span = np.array([0, 1]) # time (Year)
y0 = np.concatenate((init_position.flatten(), init_velocity.flatten()))

#sol = solve_ivp(lambda t, state: adapter(t, state, arguments, "Newton"), t_span, y0, atol=atol, rtol=rtol)
sol = solve(lambda t, state: adapter(t, state, arguments, "Newton"), t_span, y0, N=10000)
#sol = solve_dorpi(lambda t, state: adapter(t, state, arguments, "Newton"), t_span, y0, tol=0.25, max_iter=10000)
plt.plot(sol.t[1:], sol.err)
plt.show()

sol = get_components(sol)

#plot(list(range))

# draw animation, for example 
#     draw_orbits(sol, [0, 1, 4])
#     - draw the 0, 1, 4th planet
draw_orbits(sol)

input("Exit.")