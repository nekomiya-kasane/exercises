function [pairs, M] = Find3(N)
    res = 1;
    if N == 3
        for n = 5 : 10
            G = zeros(1, n * n * 10 ^ 7);
            res = n * n * 10 ^ 7;
            for i = 1 : (n * 100)
                for j = i : (n * 100)
                    G(i ^ 3 + j ^ 3) = G(i ^ 3 + j ^ 3) + 1;
                    if G(i ^ 3 + j ^ 3) == 3
                        res = min(res, i ^ 3 + j ^ 3);
                    end
                end
            end 
            if res ~= n * n * 0.1 * 10 ^ 8
                break
            end
        end
    end
    M = res;

    pairs = zeros(N, 2);
    while true
        ind = 1;
        for i = 1 : floor(nthroot(M / 2, 3))
            a = i ^ 3;
            b = max(1, floor(nthroot(M - a, 3)));
            if a + b ^ 3 == M
                pairs(ind, 1) = i;
                pairs(ind, 2) = b;
                if ind == N
                    break;
                end
                ind = ind + 1;
            end
        end
        if ind == N
            M = res;
            break;
        end
        M = M + 1;
    end
end