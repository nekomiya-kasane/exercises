function [a, b, c, d, M] = CubicTaxicabNum(N)
    a = 0;
    b = 0;
    k = N;
    while true
        found = [false, false];
        for i = 1 : floor((k / 2) ^ (1 / 3)) 
            % we only need to scan to (k / 2) ^ (1 / 3), assuming a <= b
            ap = i ^ 3;
            bp = round((k - ap) ^ (1 / 3));
            if bp == 0
                continue;
            end
            if ap + bp ^ 3 == k % verify a ^ 3 + b ^ 3 == k
                if found(1)
                    c = i;
                    d = bp;
                    found(2) = true; % already found 2 pairs of cubes
                    break;
                end
                a = i;
                b = bp;
                found(1) = true;
            end
        end
        if sum(found) == 2
            M = k;
            return;
        end
        k = k + 1;
    end
end