A = [[-1, 1]; [1, -1000]];
f = @(t, y) A * y + [2*sin(t);1000*(cos(t)-sin(t))];

y0 = [1;2];
span = [0,30];
N = 100000;

[xs, ys] = method_ex(f, span, y0, N);
plot(xs, ys)

function [xs, ys] = method_ex(f, x_range, y0, num_steps)
    arguments
        f % real 2 col vec
        x_range
        y0 % col vec
        num_steps = 100
    end
    
    bar = waitbar(0, "sdf");
    
    h = (x_range(2) - x_range(1)) / num_steps;
    xs = x_range(1) : h : x_range(2);
    
    ys(1, :) = y0'; % col vec 2 row vec
    yps(1, :) = transpose(feval(f, xs(1), y0));

    tmp = runge_kutta_4(f, xs(1):h/1000:xs(3), y0, h / 1000)';
    ys(2, :) = tmp(1000, :);
    ys(3, :) = tmp(2000, :);
    for i = 1:3
        yps(i, :) = feval(f, xs(i), ys(i, :)')';
    end
    
    for k = 1 : num_steps - 3
        waitbar(k / (num_steps - 3), bar, "Computing " + k + "/" + (num_steps - 3));
        ys(k + 3, :) = -9/2*ys(k+2,:)+9*ys(k+1,:)-11/2*ys(k,:)+3*f(xs(k),ys(k,:)')';
        if k < num_steps
            yps(k + 3, :) = feval(f, xs(k + 3), ys(k + 3, :)')';
        end
    end
    
    close(bar);
end

function ys = runge_kutta_4(f, ts, y0, h)
    ys = zeros(2, length(ts));
    ys(:, 1) = y0;
    for n = 1 : length(ts) - 1
        k1 = feval(f, ts(n), ys(:, n));
        k2 = feval(f, ts(n) + 0.5 * h, ys(:, n) + 0.5 * h * k1);
        k3 = feval(f, ts(n) + 0.5 * h, ys(:, n) + 0.5 * h * k2);
        k4 = feval(f, ts(n) + h, ys(:, n) + h * k3);
        ys(:, n + 1) = ys(:, n) + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6;
    end
end