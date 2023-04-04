G1 = tf(5, [1, 3]);
G2 = tf(1, [1, 6]);

% Block 1
B1 = G1 * G2;

G3 = tf(0.8, 1);

% Block 2
H2 = feedback(B1, G3);

H1 = tf(30, 1);

% Block 3
B2 = H1 * H2;

% Block 4
feedback(B2, 1)