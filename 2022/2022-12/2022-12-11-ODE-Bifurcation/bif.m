clear all;

as = -1:0.05:10;

options = odeset('RelTol', 1e-7);

D1 = [];
D2 = [];
for a = as
    for j = 1:100
        x0 = rand() * 10 - 5;
        y0 = rand() * 10 - 5;
        [t, A] = ode45(@sys, [0, 100], [x0, y0], options, [], a);
        x=A(:,1);
        y=A(:,2);
        for i=floor(length(x)*3/4):length(x)-1  
            if((x(i)>=x(i-1))&&(x(i)>=x(i+1)))||((x(i)<=x(i-1))&&(x(i)<=x(i+1)))
              D1=[D1;a x(i)];
            end
            if((y(i)>=y(i-1))&&(y(i)>=y(i+1)))||((y(i)<=y(i-1))&&(y(i)<=y(i+1)))
              D2=[D2;a y(i)];
            end
        end
    end
end

figure;
scatter(D1(:, 1), D1(:, 2), 'Marker', '.')
xlabel("a")
ylabel("x")
title("(x,a) bifurcation diagram")

figure;
scatter(D2(:, 1), D2(:, 2), 'Marker', '.')
xlabel("a")
ylabel("y")
title("(y,a) bifurcation diagram")

function dx = sys(t, x, flag, a)
    dx = zeros(2, 1);
    dx(1) = -x(1) + a * x(2) - x(2) * sqrt(x(1) * x(1) + x(2) * x(2));
    dx(2) = -x(2) + x(1) * sqrt(x(1) * x(1) + x(2) * x(2));
end