%% bspline2b
function [Bx, By] = bspline2b(dx, dy, depth, drawb) 
    [Bx, By] = gen_B(dx, dy);

    figure
    dim_data = 2;  
    B = zeros(dim_data, 4);  
    plot(dx, dy, ...
        "Marker", "o", ...
        "LineStyle", "--", ...
        "MarkerEdgeColor", "#2899ED", ...
        "MarkerFaceColor", "#2899ED", ...
        "Color", "#2899ED", ...
        "MarkerSize", 3 ...
        ); % plots d,s as red circles 
    
    hold on;  
    for i = 1 : length(dx) - 3
        B(1, :) = Bx(i, :);  
        B(2, :) = By(i, :);  
        drawbezier_dc(B, depth, drawb); 
    end
    hold off; 
end