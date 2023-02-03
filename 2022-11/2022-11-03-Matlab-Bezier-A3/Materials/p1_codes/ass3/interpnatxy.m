function [dx, dy] = interpnatxy(x, y)
    N = length(x) - 1;
    A = diag(ones(1, N - 1) * 2) + diag(ones(1, N - 2), 1);
    A = A + A';
    
    % also works for N = 3
    rx = 6 * x(2 : end - 1);
    ry = 6 * y(2 : end - 1);

    rx(1) = rx(1) - x(1);
    rx(end) = rx(end) - x(end);

    ry(1) = ry(1) - y(1);
    ry(end) = ry(end) - y(end);

    dx = A \ rx;
    d1x = 2 * x(1) / 3 + dx(1) / 3;
    dnx = dx(end) / 3 + 2 * x(end) / 3;
    dx = [x(1); d1x; dx; dnx; x(end)];

    dy = A \ ry;
    d1y = 2 * y(1) / 3 + dy(1) / 3;
    dny = dy(end) / 3 + 2 * y(end) / 3;
    dy = [y(1); d1y; dy; dny; y(end)];
end