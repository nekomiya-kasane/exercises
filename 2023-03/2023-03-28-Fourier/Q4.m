clear all; close all;
%Build time
L=2;
t=-3*L:0.001:3*L;
%Build f=1
f=ones(1,length(t));
%put in your value of avgvalue=a0/2
fbar=1/2;
%set f=avg to get started
f=f*fbar;
%choose number of terms
nmax=100;
%choose p
for n=1:nmax
	%put in your cn
    e1=exp(-1i*n*pi);
    e2=exp(-1i*n*pi/2);
	
    em1=exp(1i*n*pi);
    em2=exp(1i*n*pi/2);
    cn = ((4-3*1i*n*pi)*e2-(4-1i*n*pi)*em2)/(2*n^2*pi^2);
	cminusn = ((4+3*1i*n*pi)*e2-(4+1i*n*pi)*em2)/(2*n^2*pi^2);
	%update f with next component
	f=f + cn*exp(1i*n*pi*t/L)+ cminusn*exp(-1i*n*pi*t/L);
    if(abs(imag(f))>10^-9)
        fprintf('\n oops');
    end
	%plot updated f
	plot(t,real(f));
    grid on;
end
