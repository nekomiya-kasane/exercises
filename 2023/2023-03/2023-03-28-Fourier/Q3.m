clear all; close all; clc;

L = 2; 
dt = 0.01;

ts = -3*L:dt:3*L;
ys = zeros(length(ts));
for i = 1:length(ts)
    ys(i) = f_ori(ts(i));
end

figure(1)

plot(ts, ys)
xlim([-3*L-0.5, 3*L+0.5])
ylim([-3.5, 3.5])

% Fourier
NumberOfTerms = 20;

a0=0;
f=ones(1,length(ts))*a0/2;
hold on;
grid on;
for n=1:NumberOfTerms
    an = 0;
    bn = 2*n*pi*cos(n*pi/2.)-6*n*pi*(-1)^n-8*sin(n*pi/2.);
    bn = bn / (n^2*pi^2);
    f = f+an*cos(n*pi*ts/L)+bn*sin(n*pi*ts/L);
end
plot(ts,f,'r'); 
legend(["Given Function", "Fourier Approximation"])
hold on; grid on;

function y = f_ori(t)
    if t < -2
        y = f_ori(t + 4);
    elseif t > 2
        y = f_ori(t - 4);
    elseif (t >= 1) && (t <= 2)
        y = 2*t - 1;
    elseif (t >= -2) && (t <= -1)
        y = 2*t + 1;
    else
        y = 0;
    end
end