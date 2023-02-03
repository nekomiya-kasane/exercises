%% drawbezier_dc
function drawbezier_dc(B, depth, drawb)
    [x, y] = show_decas_subdiv2(B, depth); 
    hold on; 
    if drawb == 1 
        % plot bezier segments
        plot(B(1, :), B(2, :), ...
            "MarkerEdgeColor", "#FB7700", ...
            "Marker", "x", ...
            "Color", "#7DB448" ...
            ); 
    end
    plot(x, y); 
    hold off; 
end