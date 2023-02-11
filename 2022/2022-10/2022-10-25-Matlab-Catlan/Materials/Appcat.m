function [p, q] = Appcat(N)
    catconst = 0.915965594177219;
    catconst_ceil = 0.915965594177220;

    p = 1;
    q = 1;
    for i = 1 : N
        low = floor(catconst * i);
        high = ceil(catconst_ceil * i);
        if i + low > N
            break;
        end
        for j = low : high
            if abs(p / q - catconst) > abs(j / i - catconst) && i + j <= N
                p = j;
                q = i;
            end
        end
    end
end