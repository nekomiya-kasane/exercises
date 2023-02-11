while true
    [x, y] = getpoints; 
    [dx, dy] = interpnatxy(x, y);
    depth = 7; 
    for showb = [false, true]
        bspline2b(dx, dy, depth, showb); 
        title("Part 2 (showb = " + showb + ")")
        saveas(gcf, sprintf('output_a3/showb%d_part2.png', showb)); 
    end
    [~, ~, quit] = ginput(1); 
    close all
end