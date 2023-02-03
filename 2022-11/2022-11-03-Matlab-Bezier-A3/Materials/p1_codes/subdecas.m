function [ud, ld] = subdecas(cpoly)
total = length(cpoly(1,:));
ud = zeros(2, total);
ld = zeros(2, total);
matrix_x = zeros(total, total);
matrix_y = zeros(total, total);
    for k = 1: total
        matrix_x(1, k) = cpoly(1, k);
        matrix_y(1, k) = cpoly(2, k);
    end
    for i = 2: total
        for j = 1: total+1-i
            matrix_x(i, j) = (matrix_x(i-1, j) / 2.0) + (matrix_x(i-1, j+1) / 2.0);
            matrix_y(i, j) = (matrix_y(i-1, j) / 2.0) + (matrix_y(i-1, j+1) / 2.0);
        end
    end
    for k = 1: total
        ud(1, k) = matrix_x(k, 1);
        ud(2, k) = matrix_y(k, 1);
        ld(1, k) = matrix_x(total+1-k, k);
        ld(2, k) = matrix_y(total+1-k, k);
    end
end

