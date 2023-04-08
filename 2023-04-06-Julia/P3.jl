using Plots
using LaTeXStrings
using LinearSolve, SparseArrays, Random, LinearAlgebra
using ProgressBars
using Formatting

# plotlyjs()
default(fontfamily="JuliaMono-LightItalic")

u0(x, y, t) = cos(pi * x) * sin(pi * y) * cos(t)

include("Utils.jl")

Nx = Ny = 100
L = H = 1

dx = L / (Nx - 1)
dy = H / (Ny - 1)

xs = 0:dx:L
ys = 0:dy:H

a = 1;

u_init = u0.(xs', ys, 0);

function f(t, y)
    sz = size(y)
    dy = zeros(Float64, sz);

    for i = 1 : sz[1], j = 1 : sz[2]
        if i != 1 && i != Ny
            if j == 1 # left
                dy[i, j] = -sin(t) * sin(pi * ys[i])
            end
            if j == Nx # right
                dy[i, j] = a ^ 2 * (2 * y[i, j - 1] + y[i - 1, j] + y[i + 1, j] - 4 * y[i, j]) / dx ^ 2
            end
        end
        if i == 1 || i == Ny
            dy[i, j] = 0
        end
        if i != 1 && i != Ny && j != 1 && j != Nx
            dy[i, j] = a ^ 2 * (y[i, j + 1] + y[i, j - 1] + y[i - 1, j] + y[i + 1, j] - 4 * y[i, j]) / dx ^ 2
        end
    end
    return dy
end

tspan = [0, 2]
Nt = 100000;
dt = (tspan[2] - tspan[1]) / (Nt - 1);
@elpased ts, us = RK4(f, tspan, u_init, dt);

# surface(xs, ys, us[end], 
#     opacity=0.9, 
#     title=LaTeXString(sprintf1("T = %.5f", 1.222)),
#     xlabel=L"x", ylabel=L"y", zlabel=L"u(t;x,y)",
#     xlims=[0,1], ylims=[0,1], zlims=[-1,1]
# )

anim = @animate for i = 1:200:length(us)
    surface(xs, ys, us[i], 
    opacity=0.9, 
    title=LaTeXString(sprintf1("T = %.5f", ts[i])),
    xlabel=L"x", ylabel=L"y", zlabel=L"u(t;x,y)",
    xlims=[0,1], ylims=[0,1], zlims=[-1,1]
    )
end

gif(anim, "P3.gif", fps = 50)