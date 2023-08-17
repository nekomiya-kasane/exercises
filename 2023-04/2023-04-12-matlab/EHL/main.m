NIANDU0=0.08;          
U=1.0e-11;  
           
              
R=0.05;                     
W=2.0e-5;                
G=8000;                 
A0=2.2e-8;  
E0=G/A0;                    
hertzb=(sqrt(8.0*W/pi))*R;          %Hertz????           
PH=E0*hertzb/(4*R);                 %??Hertz????
tzero=18e6;                         
u2=1.8409;
u1=1.0;

N=1000;                            
P0=linspace(0,0,N+1);           
P=linspace(0,0,N+1);            
DP=linspace(0,0,N+1);            
XP=linspace(0,0,N+1);            
H=linspace(0,0,N+1);            
F=linspace(0,0,N+1);            
B=linspace(0,0,N+1);             
DF=linspace(0,0,N+1);            
DL=linspace(0,0,N+1);            
MIDU=linspace(0,0,N+1);            %??         
NIANDU=linspace(0,0,N+1);        
CIJ=zeros(N+1,N+1);                %????             
KK=zeros(N,N);               
KK1=zeros(N+1,N+1);              
KK2=zeros(N+1,N+1);              
LNODS=zeros(N+1,2);              
 
initialization;         
for i=1:N+1 
    if(XP(i)^2<=1) 
        P0(i)=sqrt(1-XP(i)^2); 
    end 
end 
P=P0; 
DH0=1; 
MAXIT=100; 
ITER=0; 
while (abs(DH0)>0.01&&ITER<=MAXIT) 
    ITER=ITER+1; 
    IT=0; 
    EP=1; 
    while (EP>0.01&&IT<=MAXIT) 
        IT=IT+1; 
        film_thick2;          
        matrix_final;        
       DP(2:N+1)=KK\DF(2:N+1)'; 
       DH0=DP(N+1); 
       DP(N+1)=0; 
       sum2=0; 
       sum3=0; 
       for i=1:N 
           sum2=sum2+abs(DP(i)); 
           sum3=sum3+P(i); 
       end 
       EP=sum2/sum3;  
       P=P+0.4*DP;    
   end 
    H0=H0+0.3*DH0; 
end 

 


mocali=0;
for i=1:N+1                                              
                             
    NIANDU(i)=exp((log(NIANDU0)+9.67)*(-1+(1+(5.1e-9)*P(i)*PH)^0.6));     
    h(i)=H(i)*hertzb^2/R;
    yita(i)=NIANDU(i)*NIANDU0;                                                        
    tomratio(i)=asinh(yita(i)*(u2-u1)/(tzero*h(i)));
    tom(i)=tzero*tomratio(i);
    mocali=mocali+tom(i)*hertzb*(1-(-2.5))/(N);
end   

fric=mocali/(W*E0*R)

figure(1); 
plot(tom/PH,'bl-')
hold on
plot(H,'r-');    
hold on; 
plot(P,'b-');     
hold on; 
%title('????????????????????'); 
axis([1 N 0 1.5]); 
set(gca,'Xtick',[0:200:2000],'Ytick',[0:0.2:5]);     
                                                    
 
grid on;                                            
xlabel('????????'); 
ylabel('????????/??????'); 
legend('????????H','??????P',-1); 
hold off; 