G1 = tf(5, [1, 3]);
G2 = tf(1, [1, 6]);

G3 = tf(0.8, 1);

H2 = feedback(G1 * G2, G3);

H1 = tf(30, 1);

feedback(H1 * H2, 1)