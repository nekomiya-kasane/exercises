%格子玻尔兹曼实现圆柱绕流
lx = 250;
ly = 51;
% [X,Y] = meshgrid(1:250,1:51);
% Z = ones(size(X,1),size(X,2));
% mesh(X,Y,Z);
obst_x = lx/5 + 1;   %圆柱的位置x
obst_y = ly/2 + 1;   %圆柱的位置y
obst_r = ly/10 + 1;  %圆柱的半径r
uMax = 0.1;         %Poiseuille流动的最大速度
Re = 100;            %Reynolds数
kinematic_viscosity = uMax * 2 * obst_r/Re; %运动粘度
omega = 1./(3*kinematic_viscosity + 1/2);   %松弛时间
maxT = 2000;         %总的迭代次数
tPlot = 5;           %循环

%D2Q9的参数设置
t = [4/9,1/9,1/9,1/9,1/9,1/36,1/36,1/36,1/36]; %权重的设置
cx = [0,1,0,-1,0,1,-1,-1,1];    %x方向的格点速度方向
cy = [0,0,1,0,-1,1,1,-1,-1];    %y方向的格点速度方向
opp = [1,4,5,2,3,8,9,6,7];      %这里是反弹边界,对应的反弹格点的位置
col = [2:(ly - 1)];
[y,x] = meshgrid(1:ly,1:lx);    %生成网格
obst = abs(x - obst_x) + abs(y - obst_y) <= obst_r;
obst = (abs(x - obst_x) + abs(y - obst_y) <= obst_r) + (abs(x - 2 * obst_x) + abs(y - obst_y) <= obst_r);
obst(:,[1,ly]) = 1;
bbRegion = find(obst);

%初始条件
fln = reshape(t' * ones(1,lx*ly),9,lx,ly); %fln是概率密度函数(分布函数)

%主循环
for cycle = 1:maxT
    %宏观量
    rho = sum(fln);
    ux = reshape(cx*reshape(fln,9,lx*ly),1,lx,ly)./rho; %x方向的速度
    uy = reshape(cy*reshape(fln,9,lx*ly),1,lx,ly)./rho; %y方向的速度
    %宏观的狄利克雷边界
    %入口：Poiseuille图像
    L = ly - 2;
    y = col - 1.5;
    ux(:,1,col) = 4 * uMax/(L*L) * (y.*L - y.*y);
    uy(:,1,col) = 0;
    rho(:,1,col) = 1./(1 - ux(:,1,col)) .* (sum(fln([1,3,5],1,col)) + 2*sum(fln([4,7,8],1,col)));
    %Outlet: Zero gradient on rho/ux
    %这是一种边界条件
    rho(:,lx,col) = rho(:,lx - 1,col);
    uy(:,lx,col) = 0;
    ux(:,lx,col) = ux(:,lx - 1,col);
    
    %Collision step (碰撞项)
    for i = 1:9
        %Left boundary
        cu = 3*(cx(i) * ux + cy(i) * uy);
        fEq(i,:,:) = rho .* t(i) .* (1 + cu + 1/2 * (cu.*cu) - 3/2 * (ux.^2 + uy.^2));
        fOut(i,:,:) = fln(i,:,:) - omega .* (fln(i,:,:) - fEq(i,:,:));
    end
    %Microscopic boundary condition (微观的边界条件)
    for i = 1:9
        %Left boundary
        fOut(i,1,col) = fEq(i,1,col) + 18 * t(i) * cx(i) * cy(i) *...
        (fln(8,1,col) - fln(7,1,col) - fEq(8,1,col) + fEq(7,1,col));
        %Right boundary
        fOut(i,lx,col) = fEq(i,lx,col) + 18 * t(i) * cx(i) * cy(i) *...
       (fln(6,lx,col) - fln(9,lx,col) - fEq(6,lx,col) + fEq(9,lx,col));
        %Bounce back region
        fOut(i,bbRegion) = fln(opp(i),bbRegion);
    end
    
    %Streaming step. (漂移项)
    for i = 1:9
        fln(i,:,:) = circshift(fOut(i,:,:),[0,cx(i),cy(i)]);
    end
    %Visualization
    if(mod(cycle,tPlot) == 0)
        u = reshape(sqrt(ux.^2 + uy.^2),lx,ly);
        u(bbRegion) = nan;
        imagesc(u');
        axis equal off;
        drawnow
    end
end
    