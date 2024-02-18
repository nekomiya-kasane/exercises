% oscillation
ks = [0.5, 1, 1.5, 2];
n = length(ks);
sys1 = cell(1, n);
sys2 = cell(1, n);

for i = 1:n
    k = ks(i);
    G1 = tf([3*k, k], [1,0]);
    D = tf(2, 1);
    
    G2 = tf(2, [1, 0.8, 1]);
    
    B1 = G1 + D;
    B1p = G1;
    
    sys1{i} = feedback(B1 * G2, 1);
    sys2{i} = feedback(B1p * G2, 1);
end

figure('Renderer', 'painters',  'Position', [100 100 1500 600])
set(gcf,'color','w');

for i = 1:n
    subplot(2, 4, i)
    step(sys1{i}, sys2{i})
    xlabel("Time (s)")
    ylabel("Amplitude")
    title("Step Respondse k=" + string(ks(i)))
    legend(["With disturbation", "Without disturbance"])

    subplot(2, 4, n + i)
    impulse(sys1{i}, sys2{i})
    xlabel("Time (s)")
    ylabel("Amplitude")
    title("Impulse Respondse k=" + string(ks(i)))
    legend(["With disturbation", "Without disturbance"])
end
