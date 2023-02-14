function [err, pred] = final_XX() 
    % this function plot the fitting curve and the given data points,
    % and returns: 
    % 1. err - the square root of the average of the squared residual
    % 2. pred - the predicted weight of an alligator that has a snout length of 55 inches
    % as said in note.pdf, the model we choose is of the form
    %  W = c1 exp (c2 L + c3 L^2)

    Ls = [47.94; 36.97; 75.94; 30.88; 45.15; 46.06; 31.82; 42.95; 
        33.12; 35.87; 66.02; 43.82; 40.85; 41.68; 43.82];
    Ws = [130.32; 50.91; 639.06; 27.94; 79.84; 109.95; 33.12; 90.02; 
        35.87; 38.09; 365.03; 83.93; 79.84; 83.10; 70.11];
    n = length(Ls);

    % solve
    A = [ones(n, 1), Ls, Ls .^ 2];
    b = log(Ws);
    
    cs = A \ b;
    cs(1) = exp(cs(1));
    
    f = @(x) cs(1) .* exp(cs(2) .* x + cs(3) .* x .^ 2);
    hat_Ws = f(Ls);
    
    % residual
    err = sqrt(sum((hat_Ws - Ws) .^ 2) / n);
    
    % plot
    xs = (min(Ls) - 9:0.1:max(Ls) + 1)';
    ws = f(xs);
    figure;
    plot(xs, ws); % fitting curve
    hold on;
    scatter(Ls, Ws, 'Marker', 'x'); % data points
    scatter(55, f(55), 'filled'); % data points
    legend("Fitting Curve", "Data Points", "Point to Be Predicted", 'Location', 'best')
    xlabel("l (inches)")
    ylabel("W (pounds)")
    title("Fitting curve of Given Data Points (W = c_1e^{c_2L+c_3L^2})")
    hold off

    % predict
    pred = f(55);
end