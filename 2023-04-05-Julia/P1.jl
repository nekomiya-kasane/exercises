#using PyPlot
# using PlotlyJS
using Plots
using LaTeXStrings
using LinearSolve, SparseArrays, Random, LinearAlgebra
using ProgressBars

plotlyjs()
default(fontfamily="JuliaMono")

include("Utils.jl")

N = 200;
L = H = 1.0;
h = L / (N - 1);

###########################################################
# 5 point
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

# 5 points
@time sol = reshape(A \ rhs, (N, N))'

ana_sol_f(x, y) = -sin(pi * x) * sin(pi * y) / (2 * pi ^ 2);

xs = 0:h:L;
ys = 0:h:L;
surface(xs, ys, sol, 
    fill=:greens, fillalpha=0.5, 
    legend=false
)

ana_sol = ana_sol_f.(xs', ys)

plot(
    surface!(xs, ys, ana_sol , fill=:orange, fillalpha=0.5, legend=false,
        xlabel=L"$x$", ylabel=L"$y$", zlabel=L"$u(x,y)$",
        title=L"Solution of -△u=f"
    ),
    surface(xs, ys, abs.(ana_sol - sol), fillalpha=0.7, title="Error")
)

maximum(vec(abs.(ana_sol - sol))) # max error

###########################################################
# 9 points

rhs9 = zeros(Float64, size(A)[1]);

for k = 1 : N
    rhs9[id(k, 1)] = -20 * g_ij(k, 1) / (6 * h ^ 2);
    rhs9[id(k, N)] = -20 * g_ij(k, N) / (6 * h ^ 2);
    rhs9[id(1, k)] = -20 * g_ij(1, k) / (6 * h ^ 2);
    rhs9[id(N, k)] = -20 * g_ij(N, k) / (6 * h ^ 2);
end

for i = 2 : N - 1, j = 2 : N - 1
    rhs9[id(i, j)] = f_ij(i, j);
end

A9 = GenerateCoeffMatrix9Point(N, h)

@time sol9 = reshape(A9 \ rhs, (N, N))'

surface(xs, ys, sol9, 
    fill=:greens, fillalpha=0.5, 
    legend=false
)

plot(
    surface!(xs, ys, ana_sol , fill=:orange, fillalpha=0.5, legend=false,
        xlabel=L"$x$", ylabel=L"$y$", zlabel=L"$u(x,y)$",
        title=L"Solution of -△u=f"
    ),
    surface(xs, ys, abs.(ana_sol - sol9), fillalpha=0.7, title="Error")
)

maximum(vec(abs.(ana_sol - sol9))) # max

###########################################################
# meter
ns = [25, 50, 100, 200, 400, 800, 1600];
err_5 = zeros(Float64, length(ns));
time_5 = zeros(Float64, length(ns));
err_9 = zeros(Float64, length(ns));
time_9 = zeros(Float64, length(ns));

k = 1;
for n = tqdm(ns)
    N = n;
    L = H = 1.0;
    h = L / (N - 1);

    xs = 0:h:L;
    ys = 0:h:L;
    ana_sol = ana_sol_f.(xs', ys);

    A_ = GenerateCoeffMatrix5Point(N, h);
    rhs_ = zeros(Float64, size(A_)[1]);

    id = (i, j) -> (i - 1) * N + j

    for k = 1 : N
        rhs_[id(k, 1)] = -4 * g_ij(k, 1) / h ^ 2;
        rhs_[id(k, N)] = -4 * g_ij(k, N) / h ^ 2;
        rhs_[id(1, k)] = -4 * g_ij(1, k) / h ^ 2;
        rhs_[id(N, k)] = -4 * g_ij(N, k) / h ^ 2;
    end

    for i = 2 : N - 1, j = 2 : N - 1
        rhs_[id(i, j)] = f_ij(i, j);
    end
    
    time_5[k] = @elapsed A_ \ rhs_;
    sol_ = reshape(A_ \ rhs_, (N, N));
    err_5[k] = maximum(vec(abs.(ana_sol - sol_)));

    # 9 points
    A_ = GenerateCoeffMatrix9Point(N, h);
    rhs_ = zeros(Float64, size(A_)[1]);

    for k = 1 : N
        rhs_[id(k, 1)] = -20 * g_ij(k, 1) / (6 * h ^ 2);
        rhs_[id(k, N)] = -20 * g_ij(k, N) / (6 * h ^ 2);
        rhs_[id(1, k)] = -20 * g_ij(1, k) / (6 * h ^ 2);
        rhs_[id(N, k)] = -20 * g_ij(N, k) / (6 * h ^ 2);
    end
    
    for i = 2 : N - 1, j = 2 : N - 1
        rhs_[id(i, j)] = f_ij(i, j);
    end   

    time_9[k] = @elapsed A_ \ rhs_
    sol_ = reshape(A_ \ rhs_, (N, N))
    err_9[k] = maximum(vec(abs.(ana_sol - sol_)))

    k += 1
end

plot(ns, err_5, xaxis=:log, yaxis=:log, label="5 Point Stencil")
p1 = plot!(ns, err_9, title="Error of 5/9 point stencil", label="9 Point Stencil")

plot(ns, time_5, xaxis=:log, yaxis=:log, label=nothing)
p2 = plot!(ns, time_9, title="Time cost of 5/9 point stencil", label=nothing)

plot(p1, p2, legend=:bottomright)

###########################################################
# SOR for 5 point stencil: not work

N = 30;
L = H = 1.0;
h = L / (N - 1);

xs = 0:h:L;
ys = 0:h:L;
ana_sol = ana_sol_f.(xs', ys);

A = GenerateCoeffMatrix5Point(N, h);
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

time1 = @elapsed sol1 = A \ rhs
time2 = @elapsed sol2 = sor(A, rhs, zeros(Float64, length(rhs)), 200, 1e-10, 0.6)[1]
sol1 = reshape(sol1, (N, N));
sol2 = reshape(sol2, (N, N));
err = maximum(vec(abs.(ana_sol - sol1)))
err = maximum(vec(abs.(ana_sol - sol2)))

