clear all; 

global f;
global fp;
global fpp;

f = @(x, y) 4.*x.^2-4*x.*y+2*y.^2+x-y;
fp = @(x, y) [1 + 8*x - 4*y, -1 - 4*x + 4*y];
fpp = @(x, y) [[8, -4],[-4, 4]];

global tol;
tol = 1e-10;

x0 = [-2, -2];

xs = [x0];
vals = [f(x0(1), x0(2))];

i = 0;
max_iter = 100;
while i < max_iter
    i = i + 1;
    [status, a, cbar] = fa(x0);
    x0 = x0 - a * cbar;
    sz = size(xs);
    xs(sz(1) + 1, :) = x0;
    vals(sz(1) + 1, :) = f(x0(1), x0(2));
    
    if ~status
        break;
    end
end

[mx, my] = meshgrid(-3:0.01:3, -3:0.01:3);
mz = f(mx, my);

figure(1)
contour(mx, my, mz, 30);
hold on;
plot(xs(:, 1), xs(:, 2));
scatter([0], [1/4], 'LineWidth',1.5, 'MarkerFaceColor', [0 .5 .5])
title("Newton Method with Dynamic \alpha")
hold off

figure(2);
plot(vals + 1/8)
title("Convergence Error")
xlabel("Iteration")
ylabel("f(x,y) - 1/8")
set(gca, 'YScale', 'log')

function [res, a, cbar] = fa(X)
    global fp;
    global tol;
    
    a = 0; res = true;
    c = fp(X(1), X(2));
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