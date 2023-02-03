[data, textdata] = xlsread('T928.xlsx', 'sheet1');

varname = textdata(1, 2:end);
obsname = textdata(2:end, 1);

r = corrcoef(data);
[vec, val, con] = pcacov(r);
f1 = repmat(sign(sum(vec)), size(vec, 1), 1);
vec = vec .* f1;
f2 = repmat(sqrt(val)', size(vec, 1), 1);
a = vec .* f2;
num = 2;

[b, t] = rotatefactors(a(:, 1:num), 'Method', 'varimax');
bz = [b, a(:, num + 1:end)];
gx = sum(bz .^ 2);
gxv = gx / sum(gx);
dfxsh = inv(r) * b;
F = data * dfxsh;

obsF = [obsname, num2cell(F)];
F1 = sortrows(obsF, 2);
F2 = sortrows(obsF, 3);
head = {'人名', '因子1', '因子2'};

result1 = [head; F1];
result2 = [head; F2];
plot(F(:, 1), F(:, 2), 'k.');
xlabel('因子得分1');
ylabel('因子得分2');
gname(obsname)