function theta = invKin2D(l, theta0, pos, n, mode)
    tol = 1e-6;

    k = 0;
    if mode == 0 % newton
        while k < n
            k = k + 1;

            [cur_pos, Jac] = evalRobot2D(l, theta0);

            theta0 = theta0 - (Jac \ (cur_pos - pos));
            theta = theta0;

            if norm(cur_pos - pos) < tol  
                break
            end
        end
    else % broyden
        [pos1, B] = evalRobot2D(l, theta0);
        while k < n
            k = k + 1;
            
            d1 = pos1 - pos;
            step = -B \ d1;
            theta0 = theta0 + step;

            [pos2, ~] = evalRobot2D(l, theta0);
            d2 = pos2 - pos;

            y = d2 - d1;
            B = B + ((y - B * step) * step') / (step' * step);

            pos1 = pos2;
            theta = theta0;

            if abs(norm(pos1 - pos)) < tol
                break
            end
        end
    end
end
