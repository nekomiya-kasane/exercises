clear all;
clf reset;
close all;

threshold = 4.31e-10 * 10;

ind = 1;
x0 = 1e-6;
while true
    x0 = x0 / 10;
    if x0 < threshold
        break;
    end
    ind = ind + 1;
end

disp(ind)