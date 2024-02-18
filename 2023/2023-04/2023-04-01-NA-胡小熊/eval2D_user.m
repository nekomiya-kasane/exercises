%This code is available in eval2D.m
% make sure you define n and mode, the ones
% below are for illustration
n = 100;
m = 100;

ls=[0.5,0.5]';
t=rand(2,1); %Choose some random starting point.

clf;
plotRobot2D(ls,t);
hold off;

while(1)
  desired=ginput(1)'; %Get desired position from user

  clf;
  plot(desired(1),desired(2),'*');
  hold on;
  plotRobot2D(ls,t,':');
  
  tic
  %Solve and display the position
  for i = 1:100
    t1=invKin2D(ls,t,desired,n,0); % Newton 
  end
  toc
  disp("Newton method time factor <<")

  tic
  for i = 1:100
    t2=invKin2D(ls,t,desired,n,1); % Bry 
  end
  toc
  disp("Broyden method time factor <<")

  plotRobot2D(ls,t1);
  plotRobot2D(ls,t2,"-.");
  hold off;
end

% Answer to the last question:
%   There're cases that Newton's Method converges while the Broyden's
% Method doesn't convergence, but there're also cases that Broyden's 
% Method converges but the Newton's doesn't convergence. But generally 
% and intuitively, Newton's method works better in terms of convergence.
% and moreover, Newton's method usually takes less time than Broyden's
% method.
