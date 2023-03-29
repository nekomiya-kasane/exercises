G1 = tf(1, [1, 1, 2]);
G2 = tf(1, [1, 5]);

G3 = tf(1, [1, 0]);

feedback(G1 * G2, G3)