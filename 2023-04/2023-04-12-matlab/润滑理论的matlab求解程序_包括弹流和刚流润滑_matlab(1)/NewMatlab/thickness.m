function hmin=thickness(m,n,e,P)  %±¾º¯ÊıµÄ¹¦ÄÜÊÇÇó×îĞ¡ÓÍÄ¤ºñ¶È
delta_m=2*pi/m;     %ÑØÔ²ÖÜ·½Ïò¾ùÔÈ»®·Öm¸ñ£¬Ô²ÖÜ·½ÏòµÄÎŞÁ¿¸ÙµÈ·ÖÊı
delta_n=2/n;        %ÑØÖáÏò¾ùÔÈ»®·Ön¸ñ£¬ÖáÏòµÄÎŞÁ¿¸ÙµÈ·ÖÊı
for i=1:m+1
for j=1:n+1
   H(i,j)=1+e*cos((i-1)*delta_m);
end
end      %ĞÎ³ÉÓÍÄ¤ÎŞÁ¿¸Ùºñ¶È¾ØÕó

hmin=H(1,n/2+1);    %Çó×îĞ¡ÓÍÄ¤ºñ¶È
for i=2:m
    if(H(i,n/2+1)<hmin)
        hmin=H(i,n/2+1);
    end
end