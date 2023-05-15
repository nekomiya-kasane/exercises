function dydt = Q2b1(~, y)
    v = y(1);
    u = y(2);
    dvdt = v^2 + v - u;
    dudt = 2*v - u;
    dydt = [dvdt; dudt];
end