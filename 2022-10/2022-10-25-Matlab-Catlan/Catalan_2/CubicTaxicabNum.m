function [a, b, c, d, M] = CubicTaxicabNum(N)
    pairs = zeros(2, 2);
    M = N;
    while true
        ind = 1;
        for i = 1 : floor(nthroot(M / 2, 3))
            a = i ^ 3;
            b = max(1, floor(nthroot(M - a, 3)));
            if a + b ^ 3 == M
                pairs(ind, 1) = i;
                pairs(ind, 2) = b;
                ind = ind + 1;
                if ind == 3
                    break;
                end
            end
        end
        if ind == 3
            break;
        end
        M = M + 1;
    end
    a = pairs(1,1);
    b = pairs(1,2);
    c = pairs(2,1);
    d = pairs(2,2);
end