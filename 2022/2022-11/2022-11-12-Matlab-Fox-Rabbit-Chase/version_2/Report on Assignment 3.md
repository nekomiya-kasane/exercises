# Report on Assignment 3

## Introduction

The following problem is proposed:

On the ground, there is a warehouse whose northeast and southeast vertices are located at $(-200,0)$ and $(-200,-400)$ , and a fox is initially sitting behind the house at $(-250,-550)$, tending to catch a rabbit. The rabbit is initially located at $(0,0)$ and starts heading home at $(-600,600)$ along the connecting line between it and is home.

- When the fox is behind the warehouse and cannot see the rabbit, then it heads toward the southeast corner of the warehouse;
- When the fox is on the east side of the warehouse, and cannot see the rabbit, then it heads north;
- When the fox can see the rabbit, it will run directly towards the rabbit.

These 3 rule gives us information about the direction of the fox’s velocity.

For convenient, we assume that the warehouse extends infinitely to the west.

There are 3 kinds of results:

- At some time, the fox is close enough to the rabbit, we say the rabbit is caught by the fox, and the simulation should terminate.
- At some time, the rabbit is close enough to its home, we say that the rabbit reaches its home, hence is not caught by the fox, and the simulation should terminate.
- Either the rabbit and the fox is too tired to move before any of the two possible situations above occurs, and the simulation should terminate.

## Analysis

The occurrence of the 3 kinds of results are actually fully determined by the initial positions and the velocity functions (with respect to time) of the fox and the rabbit. Before introducing velocity, we have some other issues to debate.

**How to determine whether the fox has caught the rabbit?**

Note that in this problem, by the assumptions and the initial position of fox and rabbit (fox below rabbit initially), we can conclude that before the fox catches the rabbit, the $y$ coordinate of the fox will always be less that that  of the rabbit, so here come our first rule:

- If the $y$ coordinate of the fox is larger than that of  the rabbit, then the fox has caught the rabbit.

Besides, we can give a threshold of the distance between them, so our second rule is:

- If the norm of the vector from the fox to the rabbit is less than the threshold,  then the fox has caught the rabbit.

```matlab
% check caught
if norm(state.rabbit_pos - state.fox_pos) < 0.1 ... % fox and rabbit close enough
    || state.fox_pos(2) > state.rabbit_pos(2) ... % fox above rabbit - deal with large step
    || state.fox_velocity(2) < 0 % fox stop to move
    state.caught = true; % then the fox have caught the rabbit
    break;   
end

% check rabbit returned home
if norm(state.rabbit_pos - config.rabbit_dest) < 0.1 ... % rabbit and its home close enough
    || state.rabbit_pos(2) > config.rabbit_dest(2) % rabbit above its home - deal with large step
    break; % then fox does not catch the rabbit
end
```



**How to determine whether the fox can see the rabbit?**

Assume the positions of the fox and the rabbit are $(x_1,y_1)$ and $(x_2,y_2)$ respectively, then the line’s function that connecting them can be written as $L:\dfrac{x-x_2}{x_1-x_2}=\dfrac{y-y_2}{y_1-y_2}$. The south wall of the warehouse has equation $S:y=-400=y_0$, and the east wall of the warehouse is $E:x=-200=x_0$. North: $N:y=0$.

- If $L$ intersects with $S$ and $y_1<y_0,x_1<x_0$, then the fox cannot see the rabbit. The $x$ coordinate of the intersection point is $x_s=x_2+\dfrac{(x_1-x_2)(y_0-y_2)}{y_1-y_2}$.
- If $L$ intersects with $E$ and $ 0>y_1>y_0,x_1>x_0$, then the fox cannot see the rabbit. The $y$ coordinate of the intersection point is $y_e=y_2+\dfrac{(x_0-x_2)(y_1-y_2)}{x_1-x_2}$.
- Otherwise, the fox can see the rabbit.

```matlab
function [point, dir] = check_block(fox, rabbit, config)
    ne = config.north_east;
    se = config.sorth_east;

    if fox(2) > se(2) % above bottom edge
        if (fox(2) > ne(2)) || (rabbit(1) >= fox(1)) % above top edge or rabbit on the right
            point = false;
            dir = (rabbit - fox) / norm(rabbit - fox);
            return; 
        end
        %= fox cannot see rabbit
        crossy = (rabbit(2) - fox(2)) * (ne(1) - fox(1)) / (rabbit(1) - fox(1)) + fox(2); % y_e
        if ~isinf(crossy) && crossy <= ne(2) 
            point = [ne(1), crossy]; 
            dir = [0, 1]'; % cannot see rabbit, head north
            return;
        end
    else % below bottom edge 
        %= fox cannot see rabbit
        crossx = fox(1) + (rabbit(1) - fox(1)) * (se(2) - fox(2)) / (rabbit(2) - fox(2)); % x_s
        if ~isinf(crossx) && crossx <= se(1)
            point = [crossx, se(2)];
            dir = (se' - fox) / norm(se' - fox); % cannot see the rabbit, head to the corner
            assert(length(dir(:, 1)) ~= length(dir(1, :)));
            return;
        end
    end

    %= fox can see rabbit
    point = false;
    dir = (rabbit - fox) / norm(rabbit - fox);
end
```



**How to calculate the distance?**

To compute the length of trajectory, we can refer to the arc differentiation formula $d s=\sqrt{d x^2+dy^2}$. At time $t$, suppose we have sampled $n$ points $(x_i,y_i)$ , then the length  of already passed trajectory can be calculated by as $\displaystyle L(t)=\sum_i \sqrt{(x_{i+1}- x_i)^2+(y_{i+1}-y_i)^2}$ up to time $t$.

Codes already presented in Euler steps.

**How to model this problem?**

This problem can be modeled as an ODE problem, if we know the expression of velocity vector.

Suppose the fox’s position is $P(t)$, and the rabbit’s is $Q(t)$, then $P’(t)=d(t;P,Q)v(t)$, $Q’(t)=d_r u(t)$. where $d_r$ is fixed and normalized pointing from the rabbit’s location to its home.

$d(t;P,Q)$, which is the normalized direction of the velocity of the fox, can be calculated from $P(t)$ and $Q(t)$. Besides, $v(t)$ and $u(t)$ are the size of the velocity of the fox and the rabbit, which only concerns with time, and the initial position $P(0), Q(0)$ are given.

**How to solve the ODE equations?**

We implemented two methods to solve the ODE numerically, given $y’(x)=f(x,y)$

<u>Euler Method:</u> $y_{n+1}=y_{n} + hf(x_n,y_n)$. It is an explicit formula with fixed time step size $h$. 

```matlab
function res_state = euler_step(config, state, dt)
    res_state = state;

    % get velocities
    [~, dir_fox] = check_block(state.fox_pos, state.rabbit_pos, config); % calculate direction
    dir_rabi = (config.rabbit_dest - state.rabbit_pos);
    dir_rabi = dir_rabi / norm(dir_rabi);
    res_state.rabbit_velocity = config.rabbit_velocity(state) * dir_rabi; % update velocity
    res_state.fox_velocity = config.fox_velocity(state) * dir_fox;
    
     	% prevent large end steps
    dt = min(dt, norm(config.rabbit_dest - state.rabbit_pos) / config.rabbit_velocity(state));
    dt = min(dt, norm(state.rabbit_pos - state.fox_pos) / config.fox_velocity(state));

    % update rabbit
    rabbit_delta = dt * res_state.rabbit_velocity;
    res_state.rabbit_pos = state.rabbit_pos + rabbit_delta; % key step: y_{n+1}=y_n+hf(x_n,y_n)
    res_state.rabbit_distance = state.rabbit_distance + norm(rabbit_delta);

    % update fox
    fox_delta = dt * res_state.fox_velocity;
    res_state.fox_pos = state.fox_pos + fox_delta;
    res_state.fox_distance = state.fox_distance + norm(fox_delta); % calculate new distance

    % update time
    res_state.time = state.time + dt;
end
```

<u>Modified Euler’s Method (Trapezoidal rule):</u> $\displaystyle y_{n+1}=y_n+\dfrac{h}{2}\left(f(x_n,y_n)+f(x_{n+1},y_{n+1})\right)$

```matlab
function res_state = sseuler_step(config, state, dt)
    res_state = state;
    next_state = state;

    % next_state f(x_n, y_n)
    [~, dir_fox] = check_block(state.fox_pos, state.rabbit_pos, config); % calculate direction
    dir_rabi = (config.rabbit_dest - state.rabbit_pos);
    dir_rabi = dir_rabi / norm(dir_rabi);
    next_state.rabbit_velocity = config.rabbit_velocity(state) * dir_rabi;
    next_state.fox_velocity = config.fox_velocity(state) * dir_fox;
    
     	% prevent large end steps
    dt = min(dt, norm(config.rabbit_dest - state.rabbit_pos) / config.rabbit_velocity(state));
    dt = min(dt, norm(state.rabbit_pos - state.fox_pos) / config.fox_velocity(state));

    rabbit_delta_1 = dt * next_state.rabbit_velocity;
    next_state.rabbit_pos = state.rabbit_pos + rabbit_delta_1;

    fox_delta_1 = dt * next_state.fox_velocity;
    next_state.fox_pos = state.fox_pos + fox_delta_1;
    
    next_state.time = next_state.time + dt;
    
    if norm(config.rabbit_dest - next_state.rabbit_pos) < config.tolerance ... % caught conditions
            || norm(next_state.fox_pos - next_state.rabbit_pos) < config.tolerance
        res_state = next_state;
        res_state.rabbit_distance = res_state.rabbit_distance + norm(rabbit_delta_1);
        res_state.fox_distance = res_state.fox_distance + norm(fox_delta_1);
        return;
    end
    
    % next_state2 f(x_{n+1}, y_{n+1})
    [~, dir_fox] = check_block(next_state.fox_pos, next_state.rabbit_pos, config);
    dir_rabi = (config.rabbit_dest - next_state.rabbit_pos);
    dir_rabi = dir_rabi / norm(dir_rabi);
    rabbit_velocity = config.rabbit_velocity(next_state) * dir_rabi;
    fox_velocity = config.fox_velocity(next_state) * dir_fox;
    
     	% prevent large end steps
    dt = min(dt, norm(config.rabbit_dest - state.rabbit_pos) / config.rabbit_velocity(state));
    dt = min(dt, norm(state.rabbit_pos - state.fox_pos) / config.fox_velocity(state));
    
    rabbit_delta_2 = dt * rabbit_velocity;
    fox_delta_2 = dt * fox_velocity;
    
    % update : key steps, y_{n+1}=y_n+h/2(f(x_n,y_n)+f(x_{n+1},y_{n+1})
    res_state.rabbit_velocity = next_state.rabbit_velocity;
    res_state.fox_velocity = next_state.fox_velocity;
    res_state.rabbit_pos = res_state.rabbit_pos + 0.5 * (rabbit_delta_1 + rabbit_delta_2); 
    res_state.fox_pos = res_state.fox_pos + 0.5 * (fox_delta_1 + fox_delta_2);
    res_state.rabbit_distance = res_state.rabbit_distance + norm(0.5 * (rabbit_delta_1 + rabbit_delta_2));
    res_state.fox_distance = res_state.fox_distance + norm(0.5 * (fox_delta_1 + fox_delta_2));

    % update time
    res_state.time = state.time + dt;
end
```

Generally, formula with fixed step size especially explicit formula doesn’t perform as well as implicit formula with adaptive step size, but it is easy to implement, and for this problem, it’s enough if we give a smaller tolerance.

For this problem, $y(t)=(P(t),Q(t))$ and $f(x,y)=(d(t;P,Q)v(t),d_ru(t))$.

## Result

### Question 1

In question 1, fixed velocities are provided: 

- fox’s velocity is $v(t)=16$ 
- rabbit’s is $u(t)=13$.

Simulation result (Modified Euler):

<img src="C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221124145625870.png" alt="image-20221124145625870" style="zoom:67%;" />

```tex
part 1
method: sseuler
Caught: false
Fox coordinate: 
   1.0e+02 *

  -4.483076092091689
   4.106857471640860

Rabbit coordinate: 
  -600
   600

Fox distance: 1044.1705
Rabbit distance: 848.5281
Total time: 65.2714
```

The fox didn’t catch the rabbit and ends at $(-448.308,410.686)$, ran $1044.1705$ meters. Total time $65.271$ seconds.

### Question 2

We assumed that the velocity of the fox and rabbit is proportional to the distance they have traveled  as any creature that runs long distances will become exhausted. The velocity loss is modeled as an exponential function of time. 

- The fox’s velocity is $v(t)=16\exp(-\mu_f d_1(t))$, in which $\mu_f=0.0002$, $d_1(t)$ is the distance the fox has run and exactly calculated by curve length approximation as explained in the last section.
- The rabbit’s velocity is $u(t) = 13\exp(-\mu_r d_2(t))$, in which $\mu_r=0.0008,s_{r_0}=13$, $d_2(t)$ is the distance the rabbit has run.



Simulation result (Modified Euler’s Method):

<img src="C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221124150049336.png" alt="image-20221124150049336" style="zoom:67%;" />

Euler’s Method

<img src="C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221124150442066.png" alt="image-20221124150442066" style="zoom:67%;" />

```tex
// Method 1
Catched: false
Fox coordinate: 
   1.0e+02 *

  -4.484122924507615
   4.107561626556001

Total distance: 1044.168
Total time: 65.2
Catched: true
Fox coordinate: 
   1.0e+02 *

  -5.862697763686134
   5.862668538854019

Total distance: 1271.2395
Total time: 90.46

// Method 2
Caught: true
Fox coordinate: 
   1.0e+02 *

  -5.862414078462711
   5.862413522689712

Rabbit coordinate: 
   1.0e+02 *

  -5.863054876718069
   5.863054876718069

Fox distance: 1271.2947
Rabbit distance: 829.1612
Total time: 90.4711
```

Hence the fox caught the rabbit after $90.5$ seconds at $(-586.3,586.3)$, after ran $1271.25$ meters.

