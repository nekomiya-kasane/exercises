%friction.m
function Fe= friction(m,n,P,e)

      %This program is used to calculate the friction on the surface of the journal and the bearing  
      %P is distributed pressure
delta_m=2*pi/m;
delta_n=2/n;
for i=1:m+1
       for j=1:n+1;
          H(i,j)=1+e*cos((i-1)*delta_m);
      end
end          %形成油膜无量纲厚度矩阵
B=0;
C=0;
for j=1:n
  for i=1:m
        B=B+(1/H(i,j)+3*H(i,j)*(P(i+1,j)-P(i,j))/delta_m)*delta_m*delta_n;
        if(P(i+1,j)==0)
        break;
        end
   end
end             %以上计算油膜承载区的无量纲摩擦力
for j=1:n
 for i=1:m
           if(P(i,j)==0)
              Hb=H(i,j);
              for k=i:m
                  C=C+Hb/(H(k,j))^2*delta_m*delta_n;
              end
         end
  end
end        %以上部分计算油膜破裂区的无量纲摩擦力
Fe=B+C;