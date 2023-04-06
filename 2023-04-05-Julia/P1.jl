using PyPlot
using Plots
using LinearSolve, SparseArrays, Random

include("Utils.jl")

N = 20;
L = H = 1.0;
h = L / N;

A = GenerateCoeffMatrix5Point(N, h)

# fill right
f = (x, y) -> sin(pi * x) * sin(pi * y)
f_ij = (i, j) -> f((i - 1) * h, (j - 1) * h)

g = (x, y) -> 0
g_ij = (i, j) -> g((i - 1) * h, (j - 1) * h)

id = (i, j) -> (i - 1) * N + j

rhs = zeros(Float64, size(A)[1]);

for k = 1 : N
    rhs[id(k, 1)] = -4 * g_ij(k, 1) / h ^ 2;
    rhs[id(k, N)] = -4 * g_ij(k, N) / h ^ 2;
    rhs[id(1, k)] = -4 * g_ij(1, k) / h ^ 2;
    rhs[id(N, k)] = -4 * g_ij(N, k) / h ^ 2;
end

for i = 2 : N - 1, j = 2 : N - 1
    rhs[id(i, j)] = f_ij(i, j);
end

@time sol = A \ rhs

plot(sol)
show()