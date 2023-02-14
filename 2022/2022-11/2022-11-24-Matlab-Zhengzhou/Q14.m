clear all;
clf reset;
close all;

%% 0.3, 0.36
%simulate(0.3, 0.36, true, 1)
simulate(0.3, 0.36, false, 1)

%% 0.5, 0.8
%simulate(0.5, 0.8, true, 2)
simulate(0.5, 0.8, false, 2)

function simulate(vx, vy, ani, ind)
    y0 = [0, 0]'; 
    dt = 0.001;
    advance(-1, -1, vx, vy);
    ts = 0:dt:15*60;
    ys = zeros(length(ts), 2);
    
    for i = 1 : length(ts)
        ys(i, :) = y0';
        dy = advance(1, y0);
        y0 = y0 + dt * dy;
    end
    
    fig = figure(ind);
    reset(fig);
    
    title("vs=" + vx + "  vy=" + vy); 
    
    xlim([0,20]);
    ylim([0,20]);
   
    if ~ani
        plot(ys(:,1), ys(:, 2))
        return
    end
    
    addframe(fig)
    for i = 1: length(ys2)
        addframe(fig, ys2(i, 1), ys2(i, 2), ts2(i));
    end
end

function dy = advance(t, y, vx, vy)
   arguments
       t = -1
       y = -1
       vx = -1
       vy = -1
   end
   
   persistent velx
   persistent vely
   
   if t < 0
       velx = vx;
       vely = vy;
       return;
   end
 
   if (y(1) > 20) || (y(1) < 0)
       velx = -velx;
   end
   if (y(2) > 20) || (y(2) < 0)
       vely = -vely;
   end 
  
   dy = [velx, vely]';
end

%% Add frame to animation
function img = addframe(handle, x, y, t)
    arguments
        handle
        x = false
        y = false
        t = false
    end

    persistent colors
    persistent tra
    persistent head
    persistent timer

    %= for clearing, trigger initialization
    if islogical(x) 
        colors = [];
    end
        
    %= initialization
    if isempty(colors)
        colors = zeros(6, 3);
        colors(1:6, :) = [
            [255, 131, 123] / 255;
            [160, 231, 103] / 255;
            [116, 203, 241] / 255;
            [201, 141, 233] / 255;
            [255, 169, 123] / 255;
            [253, 244, 152] / 255
        ];
        tra = animatedline(...
            'color', colors(1, :), ...
            'LineStyle','-' ...
        );
        head = animatedline(...
            'color', colors(1, :), ...
            'LineStyle','none', ...
            'Marker', '.', ...
            'MarkerSize', 20 ...
        );

        timer = annotation(handle, ...
            'textbox', [.8 .55 .2 .4], ...
            'String', '', ...
            'EdgeColor', 'none', ...
            'FontSize', 14, ...
            'Color', '#FF9400' ...
        );
    end

    %= for clearing only
    if islogical(x)
        img = [];
        return;
    end

    %= trajectory
    addpoints(tra, x, y)

    %= current pos
    clearpoints(head)
    addpoints(head, x, y)

    %= draw timer
    text = sprintf('Time: \n%.2f', t);
    set(timer, 'String', text)

    drawnow;

    %img = getframe(handle);
end