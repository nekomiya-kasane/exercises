function J = fdJacob2D(l,theta,alpha)
    J(:, 1) = evalRobot2D(l, theta + [alpha; 0]) - evalRobot2D(l, theta - [alpha; 0]);
    J(:, 2) = evalRobot2D(l, theta + [0; alpha]) - evalRobot2D(l, theta - [0; alpha]);
    J(:, 1:2) = J(:, 1:2) / (2 * alpha);
end

% answer 1: The error of the central finite difference method is o(h^2),
%   for small step size and good model (formulated by equations of good 
%   properties, such as smoothness in this problem), it is already enough.

% answer 2: This function would be called many times, but analytical 
%   derivations would be expensive and needs support for symbolic calculation. 
%   Therefore numerical method would be much faster.