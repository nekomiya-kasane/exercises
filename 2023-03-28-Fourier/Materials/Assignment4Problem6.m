clear all; close all; clc;
%set parameters
m=10;
c=...put your stuff here...;
L=2;
dt=L/100;
t=-3*L:dt:3*L;
NumberOfTerms= 50.0;

%plot external input fourier series
a0=1;
f=ones(1,length(t))*a0/2; %equate to average
hold on;
grid on;
%pause;
for n=1:NumberOfTerms
    an = ...put your stuff here...;
    bn = ...put your stuff here...;
    f=f+an*cos(n*pi*t/L)+bn*sin(n*pi*t/L);
end
plot(t,f,'r'); hold on; grid on;

%plot system response to input fourier series
a0=1;
f=ones(1,length(t))*a0/2; %equate to average
f=f/m;
hold on;
grid on;
for n=1:NumberOfTerms
    %use these definitions to simplify your final formula
    bit1=1-n^2*pi^2/4;
    bit2=n*pi*c;
    denom=bit1^2+bit2^2;
    an = ...put your stuff here...;
    bn = ...put your stuff here...;
    f=f+((...put your stuff here...)*cos(n*pi*t/L)+(...put your stuff here...)*sin(n*pi*t/L))/denom;
end
plot(t,f,'b'); hold on; grid on;
legend({'input','building response'});


