function [p, q] = Appcat(N)
    catconst = 0.915965594177219;
    
   lowerbound = 0.915965594177218;
   upperbound = 0.915965594177220;

    p = 1;
    q = 1;
    for i = 1 : N
        low = floor(lowerbound * i); % lower bound of the numerator
        high = ceil(upperbound * i); % upper bound of the numerator
        for j = low : high
            if abs(p / q - catconst) > abs(j / i - catconst) && i + j <= N
                p = j;
                q = i;
            end
        end
    end
end