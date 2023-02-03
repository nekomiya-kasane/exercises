function [lpoly2] = subdivstep(lpoly)
total = length(lpoly(1, 1,:));
len2 = length(lpoly(1,:,1));
lpoly2 = zeros(2, len2, 2 * total);
    for i = 1: total
        [ud, ld] = subdecas(lpoly(:,:,i));
        lpoly2(:,:,2*i-1) = ud;
        lpoly2(:,:,2*i) = ld;
    end
end
