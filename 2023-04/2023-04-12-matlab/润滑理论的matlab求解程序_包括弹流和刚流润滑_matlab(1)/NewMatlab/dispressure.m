function P=dispressure(e,m,n,ratio)
%This function is to calculate the pressure distribution of journal bearing without taking the deformation into account
delta_m=2*pi/m;              %沿圆周方向均匀划分m格
delta_n=2/n;                  %沿轴向均匀划分n格
for j=1:n+1                   %对各节点赋压力初值0
for i=1:m+1
 P(i,j)=0;
 Q(i,j)=0;
end
end
S=0;
T=0;
for j=2:n                     %第一次计算各内部节点的压力值
for i=2:m
A=(1+e*cos((i+1/2-1)*delta_m))^3;
B=(1+e*cos((i-1/2-1)*delta_m))^3;
C=((1/ratio)*delta_m/delta_n)^2*(1+e*cos((i-1)*delta_m))^3;
D=C;
E=A+B+C+D;
F=delta_m*e*(cos((i+1/2-1)*delta_m)-cos((i-1/2-1)*delta_m));
P(i,j)=(A*P(i+1,j)+B*P(i-1,j)+C*P(i,j+1)+D*P(i,j-1)-F)/E;
if(P(i,j)<=0)                     %引入雷诺边界条件
   for k=i:m
     P(k,j)=0;
     S=S+abs(Q(k,j));
     T=T+abs(P(i,j));
     Q(k,j)=P(k,j);
end
break;
end
S=S+abs(P(i,j)-Q(i,j));
T=T+abs(P(i,j));
Q(i,j)=P(i,j);
end	
end
while(S/T>0.001)         %循环计算各内部节点的压力值
S=0;
T=0;
for j=2:n
for i=2:m
  A=(1+e*cos((i+1/2-1)*delta_m))^3;
  B=(1+e*cos((i-1/2-1)*delta_m))^3;
  C=((1/ratio)*delta_m/delta_n)^2*(1+e*cos((i-1)*delta_m))^3;
  D=C;
  E=A+B+C+D;
  F=delta_m*e*(cos((i+1/2-1)*delta_m)-cos((i-1/2-1)*delta_m));
  P(i,j)=(A*P(i+1,j)+B*P(i-1,j)+C*P(i,j+1)+D*P(i,j-1)-F)/E;
  if(P(i,j)<=0)
     for k=i:m
         P(k,j)=0;
         S=S+abs(Q(k,j));
         T=T+abs(P(k,j));
         Q(k,j)=P(k,j);
     end
      break;
end
  S=S+abs(P(i,j)-Q(i,j));
  T=T+abs(P(i,j));
  Q(i,j)=P(i,j);
end
end
end


%P;     %此部分是当本函数单独使用时，用于绘制离散压力分布
%for i=1:m+1
 % x(i)=(i-1)*delta_m;
 %end
%for j=1:n+1
 %y(j)=(j-1)*delta_n;
 %end
%figure
%[x,y]=meshgrid(x,y)
%mesh(P)
