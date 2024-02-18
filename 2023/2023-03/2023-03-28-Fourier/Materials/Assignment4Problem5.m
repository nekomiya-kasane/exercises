clear all; close all; clc;
%set parameters
i = 1;
for gamma = [10, 1, 0.1]
    gamma_var=gamma;
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
        an = 4*(-1)^n-4*cos(n*pi/2.)-n*pi*sin(n*pi/2.);
        bn = n*pi*cos(n*pi/2.)-3*n*pi*(-1)^n-4*sin(n*pi/2.);
        an = an / (n^2*pi^2);
        bn = bn / (n^2*pi^2);
        f=f+an*cos(n*pi*t/L)+bn*sin(n*pi*t/L);
    end
    plot(t,f,'r'); hold on; grid on;
    
    %plot system response to input fourier series
    a0=1;
    f=ones(1,length(t))*a0/2; %equate to average
    f=f/gamma_var;
    hold on;
    grid on;
    for n=1:NumberOfTerms
        denom=gamma_var^2+n^2*pi^2/4; % use this form of your denominator for simplicity
        an = 4*(-1)^n-4*cos(n*pi/2.)-n*pi*sin(n*pi/2.);
        bn = n*pi*cos(n*pi/2.)-3*n*pi*(-1)^n-4*sin(n*pi/2.);
        an = an / (n^2*pi^2);
        bn = bn / (n^2*pi^2);
        f=f+((an*gamma_var-bn*n*pi/2)*cos(n*pi*t/L) ...
            +(an*n*pi/2+bn*gamma_var)*sin(n*pi*t/L))/denom;
    end
    plot(t,f,'b'); hold on; grid on;
    legend({'compound input','bloodstream level'});
end
