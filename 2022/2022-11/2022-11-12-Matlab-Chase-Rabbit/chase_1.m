clear all;
clf reset;
close all;

% parameters:
%   method:         method used to solve ODE
%       ode23, ode45, ode78, ode89, ode113, ode15s supported
%   tolerance:      tolerance passed to ODE solver, low tolerance will cause
%       unexpected results since the equation is defined piecewise
%   north_east:     north east coordinate of the rectangle obstacle
%   sorth_east:     south east coordinate of the rectangle obstacle
%   fox_init:       initial coordinate of the fox
%   rabbit_init:    initial coordinate of the rabbit
%   fox_velocity:   function for fox's velocity with respect to time
%   rabbit_velocity:
%                   function for rabbit's velocity with respect to time
%   arrow_factor:   scaling factor for velocity visualization
%   time_anime_factor:
%                   gif time scaling factor. Play 2 second's simulation
%       per second in gif if it's set 2 for example

if ~exist('output', 'dir') %= create output directory
    mkdir('output')
end
file_name = @(name) "output" + filesep + name;

config = struct( ...
    "method", "ode45", ... % use double quotation mark!
    "tolerance", 1e-6, ...
    "north_east", [-200, 0], ...
    "sorth_east", [-200, -400], ...
    "fox_init", [-250, -550], ...
    "rabbit_init", [0, 0], ...
    "rabbit_dest", [-600, 600], ...
    "fox_velocity", @(t) 15, ...
    "rabbit_velocity", @(t) 20, ...
    "arrow_factor", 10, ...
    "time_anime_factor", 3 ...
);

method_pool = ["ode45"];
for method = ["ode23", "ode78", "ode89", "ode113"]
    if exist(method) > 0
        method_pool(length(method_pool) + 1) = method;
    end
end

% part 1: constant velocity using different methods
rabi_v_func = @(t) 13;
fox_v_func = @(t) 16;
config.rabbit_velocity = rabi_v_func;
config.fox_velocity = fox_v_func;
for method = method_pool
    disp(strcat(">> part 1, method: ", method));
    config.method = method;
    
    fig = figure;
    
    hold on
    name = strcat("part-1-", method);
    title(name);
    result = simulate(config, fig, 100, 0.1, file_name(name));
    hold off
    
    disp("Catched: " + result.catched);
    disp("Fox coordinate: ");
    disp(result.fox_location);
    disp("Total distance: " + result.fox_distance);
    disp("Total time: " + result.time);
    disp(strcat("<< method: ", method));
    pause(2);
end

% part 2: constant velocity using different methods
rabi_v_func = @(t) 16250 ./ (1250 + 13 .* t);
fox_v_func = @(t) 10000 ./ (625 + 2 .* t);
config.rabbit_velocity = rabi_v_func;
config.fox_velocity = fox_v_func;
for method = method_pool
    disp(strcat(">> part 2, method: ", method));
    config.method = method;
    
    fig = figure;
    
    hold on
    name = strcat("part-2-", method);
    title(name);
    result = simulate(config, fig, 100, 0.1, file_name(name));
    hold off
    
    disp("Catched: " + result.catched);
    disp("Fox coordinate: ");
    disp(result.fox_location);
    disp("Total distance: " + result.fox_distance);
    disp("Total time: " + result.time);
    disp(strcat("<< method: ", method));
    pause(2);
end


%% Functions
function result = simulate(config, fig, time, dt, path)
    arguments
        config
        fig
        time
        dt
        path = []
    end
    path = path + ".gif";
    
    result = struct( ...
        "catched", false, ...
        "fox_location", [], ...
        "fox_distance", -1, ...
        "time", -1 ...
    );

    % prepare initial config
    rabi = config.rabbit_init;
    dir_rabi = config.rabbit_dest - rabi;
    dir_rabi = dir_rabi / norm(dir_rabi);
    
    fox = config.fox_init;
    
    v_rabi_func = config.rabbit_velocity;
    v_fox_func = config.fox_velocity;

    set(gca, 'XLim', [-700, 100], 'YLim', [-700, 700]);

    t = 0;
    
    %= initialization of animation
    addframe(config, fig);

    %= create gif
    if ~isempty(path)
        [A, map] = rgb2ind(frame2im(getframe(fig)), 256);
        imwrite(A, map, path, "gif", "LoopCount", Inf, "DelayTime", dt);
    end
    
    %= method starts with 'o'
    method_chars = char(config.method);
    if method_chars(1) == 'o'
        sol = get_solution(config, dt, time);

        %= draw solution as gif
        ts = 0:dt:time;
        ys = deval(sol, ts);
        for i = 1 : length(ts)
            vs = advance(ts(i), ys(:, i), config);
            addframe(config, fig,  ...
                ys(1 : 2, i), config.arrow_factor * vs(1 : 2), ... % rabbit
                ys(3 : 4, i), config.arrow_factor * vs(3 : 4), ... % fox
                ts(i));

            if ~isempty(path)
                [A, map] = rgb2ind(frame2im(getframe(fig)), 256);
                imwrite(A, map, path, "gif", ...
                    "WriteMode", "append", ...
                    "DelayTime", dt / config.time_anime_factor ...
                );
            end
            
            if sum(vs(3:4) == [0;0]) >= 2 && result.time < 0
                result.time = ts(i);
                break;
            end
        end
        
        % validate if fox catches rabbit
        y1 = ys(:, end);
        y2 = ys(:, end - 1);
        if norm(y1 - y2) < 0.01 * config.tolerance
            if norm(y1(1 : 2) - y1(3 : 4)) < 0.1
                result.catched = true;
            end
        end
        
        result.fox_location = ys(3 : 4, end);
        result.fox_distance = sum(vecnorm(ys(3 : 4, 2 : end) - ys(3 : 4, 1 : end - 1)));
        return;
    end
    
    % manully calculate
    % ignore this
    for i = 0: dt: time
        v_rabi = v_rabi_func(t);
        v_fox = v_fox_func(t);

        [~, dir_fox] = check_block(fox', rabi', config);

        rabi = rabi + dt * v_rabi * dir_rabi;
        fox = fox + dt * v_fox * dir_fox';

        t = t + dt;

        if norm(rabi - fox) < config.tolerance ...
            || fox(2) > rabi(2)
            result = fox;
            break;   
        end
        if norm(rabi - config.rabbit_dest) < config.tolerance ...
            || rabi(2) > config.rabbit_dest(2)
            break;
        end

        addframe(config, fig,  ...
            rabi, config.arrow_factor * v_rabi * dir_rabi, ...
            fox, config.arrow_factor * v_fox * dir_fox, ...
            t);

        if ~isempty(path)
            [A, map] = rgb2ind(frame2im(getframe(fig)), 256);
            imwrite(A, map, path, "gif", ...
                "WriteMode", "append", ...
                "DelayTime", dt / config.time_anime_factor ...
            );
        end
    end
end

%% Add frame to animation
function img = addframe(config, handle, rabbit, rabbit_v, fox, fox_v, t)
    arguments
        config
        handle
        rabbit = false
        rabbit_v = false
        fox = false
        fox_v = false
        t = false
    end

    persistent colors
    persistent ani_rabi
    persistent ani_rabi_head
    persistent ani_fox
    persistent ani_fox_head
    persistent timer
    persistent ruler
    persistent rabi_dest
    persistent fox_dir
    persistent rabi_dir

    %= for clearing, trigger initialization
    if islogical(rabbit) 
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
        ani_rabi = animatedline(...
            'color', colors(1, :), ...
            'LineStyle','-' ...
        );
        ani_rabi_head = animatedline(...
            'color', colors(1, :), ...
            'LineStyle','none', ...
            'Marker', '.', ...
            'MarkerSize', 20 ...
        );
        ani_fox = animatedline(...
            'color', colors(2, :), ...
            'LineStyle','-' ...
        );
        ani_fox_head = animatedline(...
            'color', colors(2, :), ...
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

        ruler = animatedline(...
            'color', colors(3, :), ...
            'LineStyle','--' ...
        );

        rabi_dest = animatedline(...
            'color', colors(5, :), ...
            'LineStyle','--', ...
            'Marker', 'o', ...
            'MarkerSize', 5 ...
        );

        fox_dir = annotation(handle, "arrow", "Color", colors(2, :));
        rabi_dir = annotation(handle, "arrow", "Color", colors(1, :));

    end

    %= for clearing only
    if islogical(rabbit)
        img = [];
        return;
    end

    %= draw rabbit and its trajectory
    addpoints(ani_rabi, rabbit(1), rabbit(2))
    clearpoints(ani_rabi_head)
    addpoints(ani_rabi_head, config.rabbit_init(1), config.rabbit_init(2))
    addpoints(ani_rabi_head, rabbit(1), rabbit(2))

    %= draw fox and its trajectory
    addpoints(ani_fox, fox(1), fox(2))
    clearpoints(ani_fox_head)
    addpoints(ani_fox_head, config.fox_init(1), config.fox_init(2))
    addpoints(ani_fox_head, fox(1), fox(2))

    %= draw line segment connecting rabbit and fox
    clearpoints(ruler)
    addpoints(ruler, fox(1), fox(2))
    addpoints(ruler, rabbit(1), rabbit(2))

    %= draw line segment connecting rabbit and its destination
    clearpoints(rabi_dest)
    addpoints(rabi_dest, config.rabbit_dest(1), config.rabbit_dest(2))
    addpoints(rabi_dest, rabbit(1), rabbit(2))

    %= draw rabbit's velocity vector
    set(rabi_dir, 'parent', gca)
    set(rabi_dir, 'X', [rabbit(1), rabbit(1) + rabbit_v(1)])
    set(rabi_dir, 'Y', [rabbit(2), rabbit(2) + rabbit_v(2)])

    %= draw fox's velocity vector
    set(fox_dir, 'parent', gca)
    set(fox_dir, 'X', [fox(1), fox(1) + fox_v(1)])
    set(fox_dir, 'Y', [fox(2), fox(2) + fox_v(2)])

    %= draw timer
    text = sprintf('Time: \n%.2f', t);
    set(timer, 'String', text)

    %= redraw obstacle
    delete(findobj('type', 'patch'));
    draw_house(config, colors(6, :));

    drawnow;

    %img = getframe(handle);
end

%% Check collision
function [point, dir] = check_block(fox, rabbit, config)
    %               a
    %    ----------------------
    %    |                    | b
    %    |                    |
    %    ----------------------
    %               c
    ne = config.north_east;
    se = config.sorth_east;
    % point = [0, 0];
    % dir = [0, 0];
    if fox(2) > se(2) % above bottom edge
        if (fox(2) > ne(2)) || (rabbit(1) >= fox(1)) % above top edge or rabbit on the right
            point = false;
            dir = (rabbit - fox) / norm(rabbit - fox);
            return; 
        end
        %= fox cannot see rabbit
        crossy = (rabbit(2) - fox(2)) * (ne(1) - fox(1)) / (rabbit(1) - fox(1)) + fox(2);
        if ~isinf(crossy) && crossy <= ne(2)
            point = [ne(1), crossy]; 
            dir = [0, 1]';
            return;
        end
    else % below bottom edge 
        %= fox cannot see rabbit
        crossx = fox(1) + (rabbit(1) - fox(1)) * (se(2) - fox(2)) / (rabbit(2) - fox(2));
        if ~isinf(crossx) && crossx <= se(1)
            point = [crossx, se(2)];
            dir = (se' - fox) / norm(se' - fox);
            assert(length(dir(:, 1)) ~= length(dir(1, :)));
            return;
        end
    end

    %= fox can see rabbit
    point = false;
    dir = (rabbit - fox) / norm(rabbit - fox);
end

%% Advance
function res = advance(t, arr, config)
    rabi = arr(1:2);
    fox = arr(3:4);

    %= calculate fox's velocity direction
    [~, fox_dir] = check_block(fox, rabi, config);
    
    %= calculate velocity vectors
    fox_v = config.fox_velocity(t);
    rabi_v = config.rabbit_velocity(t);
    rabi_dir = config.rabbit_dest - config.rabbit_init;
    rabi_dir = rabi_dir' / norm(rabi_dir);

    res = [rabi_v * rabi_dir; fox_v * fox_dir];

    %= if fox already catched rabbit
    %=      or rabbit already reached destination
    if norm(rabi - fox) < config.tolerance ...
        || fox(2) > rabi(2) ...
        || norm(rabi - config.rabbit_dest) < config.tolerance ...
        || rabi(2) > config.rabbit_dest(2)
        res = zeros(4, 1);
    end
end

%% Get Solution
function sol = get_solution(config, dt, time)
    method = config.method;
    if method == "ode15s"
        func = @ode15s;
    elseif method == "ode45"
        func = @ode45;
    elseif method == "ode78"
        func = @ode78;
    elseif method == "ode89"
        func = @ode89;
    elseif method == "ode113"
        func = @ode113;
    else
        func = @ode23;
    end
    
    %= apply tolerance
    opts = odeset('RelTol', config.tolerance,'AbsTol', config.tolerance);
    
    %= solving
    sol = func(@(t, y) advance(t, y, config), ...
        0:dt:time, [config.rabbit_init config.fox_init], ...
        opts);
end

%% Draw obstacle
function draw_house(config, color) 
    arguments
        config
        color = [0.5, 0.5, 0.5]
    end
    ne = config.north_east;
    se = config.sorth_east;
    xs = [-1000, -1000, ne(1), se(1)];
    ys = [se(2), ne(2), ne(2), se(2)];
    patch(xs, ys, color, ...
        "EdgeColor", color, "EdgeAlpha", 0.4, ...
        "FaceColor", color, "FaceAlpha", 0.4 ...
    );
end
