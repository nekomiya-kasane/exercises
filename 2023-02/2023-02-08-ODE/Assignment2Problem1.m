clear all; close all; clc;
%Assignment 2 Problem 1
tmax=25; %max time
dt=tmax/1000;% sampling width or delta t
t=0:dt:tmax; % vector (array) of time samples

%set parameters
T0=1; % initial temp
tp=1; % tau p
tw=5; % tau w
A=0.1; % A value
B=1.0; % B value
C=1.0; % C value
w=2*pi; % omega
% set D for initial condition
D=T0-A*tw/(tp+tw)-B-C/(1+tp^2*w^2);

% temperature solution
T=D*exp(-t/tp)+A*tw*exp(t/tw)/(tp+tw)+C*(cos(w*t)+tp*w*sin(w*t))/(1+tp^2*w^2)+B;

% plot temperature
plot(t,T);
yline([1.5*T0,3*T0,4*T0])
grid on;
