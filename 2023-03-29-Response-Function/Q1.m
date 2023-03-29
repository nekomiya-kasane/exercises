p1 = @(s) s^6+2*s^5+4*s^4+3*s^3+s^2+3*s+2;
p2 = @(s) 5*s^2+9*s+1;

p1c = [1, 2, 4, 3, 1, 3, 2];
p2c = [5, 9, 1];

disp("(1) roots of p:")
disp(roots(p1c))

disp("(2) roots of p:")
disp(roots(p2c))