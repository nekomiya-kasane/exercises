function [Bx, By] = show_bspline2b2(dx, dy) 
    % This is an auxilary function designed to output Bx and By 
    % for the version that uses dx and dy as input instead of 
    % % drawb = 1, shows Bezier control polygons 
    % % nn = subdivision level for de Casteljau 

    N = size(dx, 1) - 1;  
    drawb = true;  
    depth = 6;
    [Bx, By] = bspline2b(dx, dy, N, depth, drawb); 
    hold off
end

