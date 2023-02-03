function [lnodes] = makelist(lpoly)
total = length(lpoly(1,:,1));
lnodes = zeros(2, (total-1)*length(lpoly(1,1,:))+1);
for i = 1: total
    lnodes(:,i) = lpoly(:,i,1);
end
for j = 2: length(lpoly(1,1,:))
    for k = 2: total
        cur = ((j - 2) * (total-1) + (k - 1)) + total;
        lnodes(:,cur) = lpoly(:,k,j);
    end
end
