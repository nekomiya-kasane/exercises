function [Bx, By] = show_bspline2b2(dx, dy) 

    N = size(dx, 1) - 1;  
    drawb = true;  
    depth = 6;
    [Bx, By] = bspline2b(dx, dy, N, depth, drawb); 
    hold off
end

