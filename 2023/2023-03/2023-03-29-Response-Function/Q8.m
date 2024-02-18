% oscillation
ks = [-0.05, 0, 1, 2, 2.05];
n = length(ks);
sys = cell(1, n);
for i = 1:n
    G = tf([ks(i), 10 * ks(i)], [1, 4, 3, 0]);
    H = tf(1, 1);
    T = feedback(G, H);
    sys{i} = T;
end

figure('Renderer', 'painters',  'Position', [100 100 1500 600])
set(gcf,'color','w');
for i = 1:n
    subplot(2, 5, i)
    step(sys{i}, 50)
    title("Step Respondse k=" + string(ks(i)))
    subplot(2, 5, n + i)
    impulse(sys{i}, 50)
    title("Impulse Respondse k=" + string(ks(i)))
end