o1 = [1, 2];
u1 = [1, 16, 6];
o2 = [1, 3, 5];
u2 = [1, 2, 14, 3];
G1 = tf(o1, u1);
G2 = tf(o2, u2);

disp("Poles/Zeros map of G1")
figure(1)
pzmap(G1)
grid on
disp("Zeros:")
roots(o1)
disp("Poles:")
roots(u1)

disp("Poles/Zeros map of G2")
figure(2)
pzmap(G2)
grid on
disp("Zeros:")
roots(o2)
disp("Poles:")
roots(u2)
