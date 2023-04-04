clear all; close all; clc;
% you fill in bits that you say '...put your stuff here...'
% Keep a semi-colon at end of each line to suppress output to the command
% window. If you want to see the output, then remove the semi-colon
L=2;
dt=L/100;
t=-3*L:dt:3*L;
NumberOfTerms= 20;
a0=...put your stuff here...;
f=ones(1,length(t))*a0/2; %equate to average
hold on;
grid on;
%pause;
for n=1:NumberOfTerms
    an = ...put your stuff here...;
    bn = ...put your stuff here...;;
    f=f+an*cos(n*pi*t/L)+bn*sin(n*pi*t/L);
end
plot(t,f); hold on; grid on;

