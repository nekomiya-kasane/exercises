using Plots
using LaTeXStrings
using LinearSolve, SparseArrays, Random, LinearAlgebra
using ProgressBars

plotlyjs()
default(fontfamily="JuliaMono")

include("Utils.jl")

function gc(i, j, N, L)
    h = L / (N - 1);
    x = j * h; y = i * h;
    if j == 1 && i != 1 && i != N
        return -5 * sin(pi * y) * sin(-10 * y)
    elseif j == N && i != 1 && i != N
        return 5 * sin(pi * y) * sin(5-10 * y)
    else
        return 0
    end
end

ana_sol_u = (x, y) -> sin(pi * (y - 1)) * cos(5 * x - 10 * y)
f = (x, y) -> 20 * pi * cos(pi * y) * sin(5 * x - 10 * y) - (125 + pi ^ 2) * cos(5 * x - 10 * y) * sin(pi * y)
f_ij = (i, j) -> f(j * h, i * h)

N = 1000;
L = H = 1.0;
h = L / (N - 1);

id = (i, j) -> (i - 1) * N + j

A = GenerateCoeffMatrix5PointSec2(N, h, gc, id)

rhs = zeros(Float64, size(A)[1]);

for k = 1 : N
    rhs[id(1, k)] = -4 * gc(1, k, N, L) / h ^ 2;
    rhs[id(N, k)] = -4 * gc(N, k, N, L) / h ^ 2;
end

for i = 2 : N - 1, j = 1 : N
    rhs[id(i, j)] = f_ij(i, j);
end

for i = 2 : N - 1, j = [1, N]
    rhs[id(i, j)] += 2 * gc(i, j, N, L) / h;
end

@elapsed sol = A \ rhs

xs = 0:h:L;
ys = 0:h:L;
sol = reshape(sol, N, N)'
ana_sol = ana_sol_u.(xs', ys)

maximum(vec(abs.(ana_sol - sol))) # max

surface(xs, ys, sol, 
    fill=:greens, fillalpha=0.7, 
    legend=false
)

plot(
    surface!(xs, ys, ana_sol , fill=:orange, fillalpha=0.5, legend=false,
        xlabel=L"$x$", ylabel=L"$y$", zlabel=L"$u(x,y)$",
        title=L"Solution of -△u=f",
        size=(1200, 600)
    ),
    surface(xs, ys, abs.(ana_sol - sol), fillalpha=0.7, title="Error")
)

1 + 1