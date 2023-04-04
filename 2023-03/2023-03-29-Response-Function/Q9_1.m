k = 0.5;

G1 = tf([3*k, k], [1,0]);
D = tf(2, 1);

G2 = tf(2, [1, 0.8, 1]);

B1 = G1 * D;

sys = feedback(B1 * G2, 1)

set(gcf,'color','w');

subplot(2, 1, 1)
step(sys)
xlabel("Time (s)")
ylabel("Amplitude")
title("Step function response")

subplot(2, 1, 2)
impulse(sys)
xlabel("Time (s)")
ylabel("Amplitude")
title("Impulse function response")
