%flow_quantity.m
function[Q1,Q2,Q3]=flow_quantity(m,n,e,ratio,P) 
%This program is used to calculate the flow quantity of the sliding bearing 
%P is distributed pressure
    delta_m=2*pi/m;
    delta_n=2/n;
    H0=(1+e);
    
    Q1=0;
  for j=1:n
      Q1=Q1+(P(2,j)-P(1,j))/delta_m*delta_n;
end
      Q1=H0/2-H0^3*Q1/4;       %计算轴承油膜起始边的进油量
      
for i=1:m
      if(P(i,2)==0)
      break;
     end
end                 %找到油膜终止边的位置
  Hb=(1+e*cos((i-1)*delta_m));
   Q2=Hb/2;                  %计算轴承油膜终止边的出油量
   
  Q3=0;
for k=1:m
      Hi=(1+e*cos((k-1)*delta_m));
      Q3=Q3+Hi^3*(P(k,n)-P(k,n+1))/delta_n*delta_m; 
        %计算轴承两端的端泄量
end
Q3=Q3/(2*ratio^2);