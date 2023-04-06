using SparseArrays

function GenerateCoeffMatrix5Point(N::Int64, h::Float64)
    allocator = (i, j) -> (i - 1) * N + j;
    return GenerateCoeffMatrix5Point(N, h, allocator)
end

function GenerateCoeffMatrix5Point(N::Int64, h::Float64, allocator::Function)
    nonzero_size = (N - 4) * (N - 4) * 5 + (N - 4) * 4 * 4 + 4 * 3 + N * 4 - 4
    ids_row = zeros(Int64, nonzero_size);
    ids_col = zeros(Int64, nonzero_size);

    values = zeros(Float64, nonzero_size);

    row = 1;
    count = 1;
    for i = 1 : N, j = 1 : N
        if i != 1 && i != N && j != 1 && j != N
            if i - 1 > 1 # up
                ids_row[count] = row;
                ids_col[count] = allocator(i - 1, j);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            if i + 1 < N # down
                ids_row[count] = row;
                ids_col[count] = allocator(i + 1, j);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            if j - 1 > 1 # left
                ids_row[count] = row;
                ids_col[count] = allocator(i, j - 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            if j + 1 < N # right
                ids_row[count] = row;
                ids_col[count] = allocator(i, j + 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
        end

        # center
        ids_row[count] = row;
        ids_col[count] = allocator(i, j);
        values[count] = -4 / h ^ 2; 
        count += 1;

        # next equation
        row += 1;
    end

    return sparse(ids_row, ids_col, values);
end

function GenerateCoeffMatrix9Point(N::Int64, h::Float64)
    allocator = (i, j) -> (i - 1) * (N - 2) + j;
    return GenerateCoeffMatrix9Point(N, h, allocator);
end

function GenerateCoeffMatrix9Point(N::Int64, h::Float64, allocator::Function)
    nonzero_size = (N - 4) * (N - 4) * 9 + (N - 4) * 4 * 6 + 4 * 4
    ids_row = zeros(Int32, nonzero_size);
    ids_col = zeros(Int32, nonzero_size);

    values = zeros(Float64, nonzero_size);

    row = 1;
    count = 1;
    for i = 2 : N - 1, j = 2 : N - 1
        if i - 1 > 1 
            if j - 1 > 1 # top-left
                ids_row[count] = row;
                ids_col[count] = allocator(i - 1, j - 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            if j + 1 < N # top-right
                ids_row[count] = row;
                ids_col[count] = allocator(i - 1, j + 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            ids_row[count] = row; # top-center
            ids_col[count] = allocator(i - 1, j);
            values[count] = 4 / h ^ 2;
            count += 1;
        end
        if i + 1 < N
            if j - 1 > 1 # bottom-left
                ids_row[count] = row;
                ids_col[count] = allocator(i + 1, j - 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            if j + 1 < N # bottom-right
                ids_row[count] = row;
                ids_col[count] = allocator(i + 1, j + 1);
                values[count] = 1 / h ^ 2;
                count += 1;
            end
            ids_row[count] = row;  # bottom-center
            ids_col[count] = allocator(i + 1, j);
            values[count] = 4 / h ^ 2;
            count += 1;
        end
        if j - 1 > 1 # left
            ids_row[count] = row;
            ids_col[count] = allocator(i, j - 1);
            values[count] = 4 / h ^ 2;
            count += 1;
        end
        if j + 1 < N # right
            ids_row[count] = row;
            ids_col[count] = allocator(i, j + 1);
            values[count] = 4 / h ^ 2;
            count += 1;
        end

        # center
        ids_row[count] = row;
        ids_col[count] = allocator(i, j);
        values[count] = -20 / h ^ 2; 
        count += 1;

        # next equation
        row += 1;
    end

    return sparse(ids_row, ids_col, values);
end

