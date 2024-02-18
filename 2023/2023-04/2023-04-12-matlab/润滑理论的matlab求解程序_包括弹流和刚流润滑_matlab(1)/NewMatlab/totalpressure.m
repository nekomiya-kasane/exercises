function[W,angle]= totalpressure(m,n,P)   
%This function is used to calculate the total pressure of the bearing and the angle 

delta_m=2*pi/m;
delta_n=2/n;
Wx=0;
Wy=0;
for j=1:n
   for i=1:m
        Wx=Wx+P(i,j)*delta_m*delta_n*cos((i-1)*delta_m);
        Wy=Wy+P(i,j)*delta_m*delta_n*sin((i-1)*delta_m);
   end
end
W=sqrt(Wx^2+Wy^2);
angle=atan(abs(Wy/Wx))*180/pi;