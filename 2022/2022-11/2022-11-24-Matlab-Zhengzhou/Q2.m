clear all;
clf reset;
close all;

f = @(x) x.^6/sqrt(6+x) + exp(x);

h = 0.001;
xs = 0:h:1;
ys = f(xs);

head = ys(1:end-1);
tail = ys(2:end);

int = sum(0.5 * (head + tail) * h);
disp("Integrate of f(x): " + int);

%% fitting
xs = xs';
n = length(xs);
A = [zeros(n, 1) xs xs.^2 xs.^3 xs.^4 xs.^5];
b = ys';

coeff = A \ b;

g = @(x) coeff(1) + coeff(2)*x + coeff(3)*x.^2 + ...
    coeff(4)*x.^3 + coeff(5)*x.^4 + coeff(6)*x.^5;

yfs = g(xs);

figure;
plot(xs, ys);
hold on
plot(xs, yfs);
legend("Given curve", "Fitting curve")
xlabel("x")
ylabel("y")
hold off