using SparseArrays
using LinearAlgebra

function GenerateCoeffMatrix5Point(N::Int64, h::Float64)
    allocator = (i, j) -> (i - 1) * N + j
    return GenerateCoeffMatrix5Point(N, h, allocator)
end

function GenerateCoeffMatrix5Point(N::Int64, h::Float64, allocator::Function)
    nonzero_size = (N - 2) * (N - 2) * 5 + 4 * N - 4
    ids_row = zeros(Int64, nonzero_size)
    ids_col = zeros(Int64, nonzero_size)

    values = zeros(Float64, nonzero_size)

    row = 1
    count = 1
    for i = 1:N, j = 1:N
        if i != 1 && i != N && j != 1 && j != N
            ids_row[count] = row
            ids_col[count] = allocator(i - 1, j)
            values[count] = 1 / h^2
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i + 1, j)
            values[count] = 1 / h^2
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i, j - 1)
            values[count] = 1 / h^2
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i, j + 1)
            values[count] = 1 / h^2
            count += 1
        end

        # center
        ids_row[count] = row
        ids_col[count] = allocator(i, j)
        values[count] = -4 / h^2
        count += 1

        # next equation
        row += 1
    end

    return sparse(ids_row, ids_col, values)
end

function GenerateCoeffMatrix9Point(N::Int64, h::Float64)
    allocator = (i, j) -> (i - 1) * N + j
    return GenerateCoeffMatrix9Point(N, h, allocator)
end

function GenerateCoeffMatrix9Point(N::Int64, h::Float64, allocator::Function)
    nonzero_size = (N - 2) * (N - 2) * 9 + N * 4 - 4
    ids_row = zeros(Int64, nonzero_size)
    ids_col = zeros(Int64, nonzero_size)

    values = zeros(Float64, nonzero_size)

    row = 1
    count = 1
    for i = 1:N, j = 1:N
        if i != 1 && i != N && j != 1 && j != N
            ids_row[count] = row
            ids_col[count] = allocator(i - 1, j - 1)
            values[count] = 1 / (6 * h^2)
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i - 1, j + 1)
            values[count] = 1 / (6 * h^2)
            count += 1

            ids_row[count] = row # top-center
            ids_col[count] = allocator(i - 1, j)
            values[count] = 4 / (6 * h^2)
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i + 1, j - 1)
            values[count] = 1 / (6 * h^2)
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i + 1, j + 1)
            values[count] = 1 / (6 * h^2)
            count += 1

            ids_row[count] = row  # bottom-center
            ids_col[count] = allocator(i + 1, j)
            values[count] = 4 / (6 * h^2)
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i, j - 1)
            values[count] = 4 / (6 * h^2)
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i, j + 1)
            values[count] = 4 / (6 * h^2)
            count += 1
        end

        # center
        ids_row[count] = row
        ids_col[count] = allocator(i, j)
        values[count] = -20 / (6 * h^2)
        count += 1

        # next equation
        row += 1
    end

    return sparse(ids_row, ids_col, values)
end

function sor_(A, b, x0, nmax, tol, omega)
    (n, _) = size(A)

    iter = 0
    r = b - A * x0
    err = norm(r)
    xold = x0

    x = zeros(Float64, n)
    errs = zeros(0)

    while err > tol && iter < nmax
        # display(iter)
        iter += 1
        for i = 1:n
            s = 0
            for j = 1:i-1
                s = s + A[i, j] * x[j]
            end
            for j = i+1:n
                s = s + A[i, j] * xold[j]
            end
            x[i] = omega * (b[i] - s) / A[i, i] + (1 - omega) * xold[i]
        end
        xold = x
        r = b - A * x
        append!(errs, norm(r, Inf))
    end
    return (x, errs)
end

function sor(A::Array{Float64,2}, b::Array{Float64,1}, x0::Array{Float64,1}, maxiter::Int64, tol::Float64, omega::Float64)
    n = size(A, 1)
    x = copy(x0)
    for k = 1:maxiter
        for i = 1:n
            sigma = 0.0
            for j = 1:i-1
                sigma += A[i,j]*x[j]
            end
            for j = i+1:n
                sigma += A[i,j]*x0[j]
            end
            x[i] = (1-omega)*x0[i] + omega*(b[i]-sigma)/A[i,i]
        end
        if norm(x-x0) < tol
            break
        end
        x0 = copy(x)
    end
    return x
end

function GenerateCoeffMatrix5PointSec2(N::Int64, h::Float64, g::Function)
    allocator = (i, j) -> (i - 1) * N + j
    return GenerateCoeffMatrix5PointSec2(N, h, g, allocator)
end

function GenerateCoeffMatrix5PointSec2(N::Int64, h::Float64, g::Function, allocator::Function)
    nonzero_size = (N - 2) * (N - 2) * 5 + 4 * (N - 2) * 2 + 2 * N
    ids_row = zeros(Int64, nonzero_size)
    ids_col = zeros(Int64, nonzero_size)

    values = zeros(Float64, nonzero_size)

    row = 1
    count = 1
    for i = 1:N, j = 1:N
        if i != 1 && i != N
            ids_row[count] = row
            ids_col[count] = allocator(i - 1, j)
            values[count] = -1 / h^2
            count += 1

            ids_row[count] = row
            ids_col[count] = allocator(i + 1, j)
            values[count] = -1 / h^2
            count += 1    

            if j != 1
                ids_row[count] = row
                ids_col[count] = allocator(i, j - 1)
                if j == N
                    values[count] = -2 / h^2
                else
                    values[count] = -1 / h^2
                end
                count += 1
            end
            if j != N
                ids_row[count] = row
                ids_col[count] = allocator(i, j + 1)
                if j == 1
                    values[count] = -2 / h^2
                else
                    values[count] = -1 / h^2
                end
                count += 1
            end
        end

        # center
        ids_row[count] = row
        ids_col[count] = allocator(i, j)
        values[count] = 4 / h^2
        count += 1

        # next equation
        row += 1
    end

    return sparse(ids_row, ids_col, values)
end

function RK4(f::Function, tspan, y0, h)
    t = tspan[1]
    ys = typeof(y0)[]
    ts = typeof(h)[]
    push!(ys, y0)
    push!(ts, t)
    while t < tspan[2]
        k1 = f(t, ys[end])
        k2 = f(t + h / 2., ys[end] + h * k1 / 2)
        k3 = f(t + h / 2., ys[end] + h * k2 / 2)
        k4 = f(t + h, ys[end] + h * k3)
        
        #y_new = ys[end] + f(t, ys[end]) * h;
        y_new = ys[end] .+ (k1 .+ 2 .* k2 .+ 2 .* k3 .+ k4) .* h ./ 6
        t += h

        push!(ys, y_new)
        push!(ts, t)
    end
    return ts, ys
end