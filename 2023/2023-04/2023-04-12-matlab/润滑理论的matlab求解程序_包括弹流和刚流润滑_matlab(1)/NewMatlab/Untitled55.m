clear
%bearingfeature.m
% This program is used to calculate the feature of journal bearing without taking the elastic deformation into account 
% e is the eccentricity 
% ratio is the ratio of L/D
% m is the number of columns
% n is the number of rays 
% S is the sum of difference between P (k) and P(k-1)
% T is the sum of P(k)
% r is the radius of the bearing journal 
% W is the total of pressure 
e=input('enter the eccentricity e=')
ratio=input('enter the ratio of L/D ratio=')
m=input('enter the number of columns m=')
n=input('enter the number of rays n=' )

[l,k]=size(e);                      %ÇóÊäÈëÆ«ĞÄÂÊÏòÁ¿µÄÎ¬Êı
[l,s]=size(ratio);    %ÇóÊäÈë¿í¾¶±ÈÏòÁ¿µÄÎ¬Êı

H1=figure;
H2=figure;
H3=figure;
H4=figure;
H5=figure;
H6=figure;

%Ñ­»·¼ÆËãÔÚ²»Í¬µÄ¿í¾¶±ÈºÍ²»Í¬µÄÆ«ĞÄÂÊµÄÇé¿öÏÂµÄÎŞÁ¿¸Ù³ĞÔØÄÜÁ¦ºÍÆ«Î»½Ç
for j=1:s
   for i=1:k
    
     P=dispressure(e(i),m,n,ratio(j));
         %disp(¡®Begin to test,press return to ¡­.¡¯);
         %keyboard;
          hmin=thickness(m,n,e(i),P); 
          Pmax=pressness(P);
         [Hr,Hi]=filmrupture(P);
      [W(i),angle(i)]=totalpressure(m,n,P);
      [Q1(i),Q2(i),Q3(i)]=flow_quantity(m,n,e(i),ratio(j),P);
      Fe(i,j)=friction(m,n,P,e(i));
   end 
W;
angle;

%disp(¡®¼ì²éWºÍangleµÄÖµ¡£¡£¡£¡¯);
%keyboard;
Pmax;
hmin;
Hr;
Hi;

figure(H1);
hold on; 
plot(e,W);
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÎŞÁ¿¸Ù³ĞÔØÁ¦µÄ¹ØÏµÇúÏß');
xlabel('Æ«ĞÄÂÊ\epsilon');
ylabel('ÎŞÁ¿¸Ù³ĞÔØÁ¦W');


figure(H2);
hold on;
plot(e,angle);
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÆ«Î»½ÇµÄ¹ØÏµÇúÏß');
xlabel ('Æ«ĞÄÂÊ\epsilon');
ylabel ('Æ«Î»½Ç\psi');


figure(H3);
hold on;
plot(e,Fe(:,j));
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÎŞÁ¿¸ÙÄ¦²ÁÁ¦µÄ¹ØÏµÇúÏß');
xlabel ('Æ«ĞÄÂÊ\epsilon');
ylabel ('ÎŞÁ¿¸ÙÄ¦²ÁÁ¦F');
 

figure (H4);
hold on;
plot(e,Q3);
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÈó»¬ÓÍ¶ËĞ¹Á÷Á¿µÄ¹ØÏµÇúÏß');
xlabel('Æ«ĞÄÂÊ\epsilon');
ylabel('Èó»¬ÓÍ¶ËĞ¹Á÷Á¿Q');


figure (H5);
hold on;
plot(e,Q1);
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÖá³ĞÓÍÄ¤ÆğÊ¼±ß½øÓÍÁ¿µÄ¹ØÏµÇúÏß');
xlabel('Æ«ĞÄÂÊ\epsilon');
ylabel('Öá³ĞÓÍÄ¤ÆğÊ¼±ß½øÓÍÁ¿Q1');


figure (H6);
hold on;
plot(e,Q2);
title('²»Í¬¿í¾¶±ÈÆ«ĞÄÂÊºÍÖá³ĞÓÍÄ¤ÖÕÖ¹±ß³öÓÍÁ¿µÄ¹ØÏµÇúÏß');
xlabel('Æ«ĞÄÂÊ\epsilon');
ylabel('Öá³ĞÓÍÄ¤ÖÕÖ¹±ß³öÓÍÁ¿Q2');
end
