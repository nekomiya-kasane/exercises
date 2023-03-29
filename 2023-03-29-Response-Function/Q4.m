G1 = tf(1, [1, 2, 3]);
G2 = tf(1, [1, 1]);

feedback(G1 * G2, 1)

