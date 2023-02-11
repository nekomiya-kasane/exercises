function [c, rmse] = myLS_XX(x, y, fopt, pflag)
   % This function calculates the linear regression/fitting line of the
   % given data pairs {(xi,yi)} using least square method
   % 
   % Algorithm:
   %    - construct A as [1, x]
   %    - solve for coefficients c where Ac=y
   %    Then the fitting line is y = c^T [1;x]
   %
   % Inputs:
   %    x, y - data pair, in row/column 1 dimension vector
   %    fopt - fitting type (not used)
   %    pflag - plot it at the same time
   % Outputs:
   %    c - coeffients (y = c0 + c1 x)
   %    rmse - RMSE of the fitting, defined as 
   %            $\sqrt{\dfrac{\sum |\hat{y}-y|^2}{n}}$

   % to column vector
   sx = size(x);
   sy = size(y);

   if sx(1) == 1
       xx = x';
   else
       xx = x;
   end
   if sy(1) == 1
       yy = y';
   else
       yy = y;
   end

   % generate A
   A = aMatrix(xx, fopt);

   % solve
   c = A \ yy;

   % plot
   if pflag == 1
       span = [min(xx), max(xx)];
       ts = span(1):(span(2) - span(1))/100:span(2);
       f = @(x) c(1) + c(2) .* x;
       ys = f(ts);
    
       figure;
       scatter(xx, yy, 'Marker', 'x');
       hold on
       plot(ts, ys);
       legend("Samples", "Fitting Curve")
       title("Fitting Curve of Given Data")
       xlabel("x")
       ylabel("y")
       hold off
   end

   % RMSE
   rmse = sqrt(norm(f(xx) - yy) ^ 2 / length(xx));
end

function A = aMatrix(x, fopt)
   n = length(x);
   if length(x(:, 1)) ~= n % row vector
       A = [ones(n, 1) x'];
   else % column vector
       A = [ones(n, 1) x];
   end
end