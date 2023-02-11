function [map, M] = CubicTaxicabNum2(n)
    k = 1; % 87539319;
    map = zeros(n, 2);
    while true
        found = zeros(1, n);
        nx = 1;
        for i = 1 : floor((k / 2) ^ (1 / 3))
            % we only need to scan to (k / 2) ^ (1 / 3), assuming a <= b
            ap = i ^ 3;
            bp = round((k - ap) ^ (1 / 3));
            if bp == 0
                continue;
            end
            if ap + bp ^ 3 == k % verify a ^ 3 + b ^ 3 == k
                map(nx, 1) = i;
                map(nx, 2) = bp; % record the nx-th pair

                found(nx) = true; % already found nx pairs of cubes
                nx = nx + 1;
                if nx > n
                    break;
                end
            end
        end
        if sum(found) == n
            M = k;
            return;
        end
        k = k + 1;
    end
end