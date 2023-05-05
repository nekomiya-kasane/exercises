clear all; 

global f;

f = @(x, y) 4.*x.^2-4*x.*y+2*y.^2+x-y;

global tol;
tol = 1e-10;

hs = 10.^(-[1,2,3,4,5,6]);

xss = cell(length(hs), 1);
vals = cell(length(hs), 1);

iters = [0] * length(hs);

x0 = [-2, -2];

for i = 1:length(hs)
    xss{i} = [x0];
    vals{i} = [f(x0(1), x0(2))];
    iters(i) = 0;
end

max_iter = 200;
for i = 1 : length(hs)
    h = hs(i);
    
    j = 0;
    while j < max_iter
        j = j + 1;
        [status, a, cbar] = fa(x0, h);
        x0 = x0 - a * cbar;
        sz = size(xss{i});
        xss{i}(sz(1) + 1, :) = x0;
        vals{i}(sz(1) + 1, :) = f(x0(1), x0(2));

        if ~status
            break;
        end
    end
    
    iters(i) = j;
    
    i = i + 1;
end

[mx, my] = meshgrid(-3:0.01:3, -3:0.01:3);
mz = f(mx, my);

figure(1)
contour(mx, my, mz, 30);
hold on;
for i = 1 : length(hs)
    plot(xss{i}(:, 1), xss{i}(:, 2));
    i = i + 1;
end
scatter([0], [1/4], 'LineWidth',1.5, 'MarkerFaceColor', [0 .5 .5])
title("Newton Method with Dynamic \alpha")
legend(["Contour", "1e-1", "1e-2", "1e-3", "1e-4", "1e-5", "1e-6"])
hold off

figure(2);
for i = 1 : length(hs)
    plot(vals{i} + 1/8);
    if i == 1
        hold on
    end
    i = i + 1;
end
title("Convergence Error")
xlabel("Iteration")
ylabel("f(x,y) - 1/8")
set(gca, 'YScale', 'log')
legend(["1e-1", "1e-2", "1e-3", "1e-4", "1e-5", "1e-6"])
hold off

function res = fp(x, y, h)
    global f;
    res = [f(x+h,y) - f(x,y), f(x,y+h) - f(x,y)]/h;
end

function [res, a, cbar] = fa(X, h)
    global tol;
    
    a = 0; res = true;
    c = fp(X(1), X(2), h);
    cbar = c / norm(c, 2);
    
    if norm(c, 2) < tol
        res = false;
        return;
    end
     
    x = X(1);    y = X(2);
    cx = cbar(1); cy = cbar(2);
    a = -(4*x*(cy-2*cx)+(4*y-1)*(cx-cy))/ ...
        (8*cx*(cx-cy)+4*cy*cy);
end