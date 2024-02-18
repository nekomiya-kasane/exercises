function Pmax=pressness(P)  %本函数的功能是求最大压力
[m n]=size(P);
Pmax=P(1,1);
for i=1:m-1
    for j=1:n-1
    if(Pmax<P(i,j))
        Pmax=P(i,j);
    end
end
end

