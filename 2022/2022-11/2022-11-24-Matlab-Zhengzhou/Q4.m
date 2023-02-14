clear all;
clf reset;
close all;

syms x

disp("Analytical")

disp("First:")
limit((sqrt(x^2+1) - 3*x)/(x+sin(x)),inf)

disp("Second:")
syms x
int(sqrt(1-x)/sqrt(1+x),x,0,1)