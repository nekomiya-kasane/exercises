for i=1:N+1                                                                   
    H(i)=H0+XP(i)^2/2;
    DH(i)=0;
    for j=1:N+1
        CIJ(i,j)=-D*((i-j+0.5)*(log(abs(i-j+0.5)*D)-1)-(i-j-0.5)*(log(abs(i-j-0.5)*D)-1))/pi;
       DH(i)=DH(i)+CIJ(i,j)*P(j);                  
     end                                                          
     H(i)=H(i)+DH(i);                                       
 end                    