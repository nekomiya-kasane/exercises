# Report on *The Mighty Big Problem*

## Preliminary

For convenience, we want to use dimensionless formula to do the simulation and get rid of large exponential powers. Hence we choose the following unit system:

1. Length in **AU** -> 1AU $\approx 1.49597870\times 10^{11}$ m
2. Time in **EY (Earth Year)** -> 1EY $\approx 3.1536\times 10^7$ s
3. Angle in **Radian**
4. Mass in **EM (Earth Mass)** -> 1EM $\approx\ 5.97219\times 10^{24}$ kg 

We’re given the following data:

- Mass in kg -> divide it by earth’s mass and we’d get masses in EM.
- Semimajor radius or orbit in AU
- Eccentricity
- Period in EY (Earth Years)

and we could calculate the following two sets of key data:

- Perihelion Distance -> $a(1-e)$, with the same unit as $a$

- Initial Velocity -> at perihelion, the velocity of the planet is perpendicular to the segment connecting it and the sun. Hence for convenience, we can put all the initial position of our planets on $x$-axis, then the velocity will have zero components on $y$ and $z$ direction initially. And it can be computed by

  $v=\sqrt{GM\dfrac{1}{a}\dfrac{1+e}{1-e}}$

  according to [orbit - Calculating object velocity at perihelion - Astronomy Stack Exchange](https://astronomy.stackexchange.com/questions/34041/calculating-object-velocity-at-perihelion)

But we still lack of a key data:

- The inclination of the orbits -> I found the data from [Orbital inclination - Wikipedia](https://en.wikipedia.org/wiki/Orbital_inclination), and convert them to radians

  $x\textrm{ deg } = \dfrac{x}{180}\pi\textrm{ rad }$

By converting the units, we get the following gravity constant:

- $G=4\pi^2/M_{\text{sun}}\approx1.1875165\times 10^{-4} AU^3EY^{-2}EM^{-1}$

## Answer to 10.

HOW AWESOME IS THAT? -> We’re standing on the shoulders of giants. The human beings, though live short individually, are marching forward by inheriting civilization like a sort of eternal life. Successors always know more than the older, that’s exciting.

## Simulation

#### Part A

According to the formula:

$\displaystyle\dfrac{d^2r_m}{dt^2}=-\sum_{s\neq m}GM_s\dfrac{r_m}{r_m^3}=a_m$

for any planet, its acceleration can be computed be transverse all other planets and the sun, and add the vectors together.

We use such vector as the variable:

$[p_1,p_2,\cdots,p_k,v_1,v_2,\cdots v_k]$

where $p_i$ is the position of the i-th planet (0 for the sun), containing 3 components $(x_i,y_i,z_i)$, thanks to numpy’s reshape method, reformatting is really easy.

Then the system can be expressed as an ODE:

$\dfrac{dp_i}{dt}=v_i$, $\dfrac{dv_i}{dt}=a_i$

Thus we can make use of `scipy`‘s `solve_ivp` method to get $v,a$ at any time. Here we passed tolerance as `1e-8` and `1e-11`. and interpolate it into uniform steps.

the result orbit looks like this:

<center>Fig 1. Orbit of mercury under Newton’s Theory</center>

![image-20221118064330753](C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221118064330753.png)

Also, we can plot it in the polar coordinate:

<center>Fig 2. Orbit of mercury under Newton’s Theory (Polar)</center>

![image-20221118064440543](C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221118064440543.png)

### Part B:

The planet that affects mercury most should be the one that maximizes $\dfrac{M_{\text{other}}}{r^2}$, as Jupyter is at least 200 times heavier than other planets, while its orbit’s semimajor radius is at most 10 AU (upper bound), therefore we can confirm that it affects mercury most.

After adding all the planets, we get the following orbits:

<center>Fig 3. Orbits of the solar system</center>

<center>Fig 3. Orbits of the solar system</center>

![image-20221118070438872](Report%20on%20The%20Mighty%20Big%20Problem.assets/image-20221118070438872.png)

And we verified that Juputer affected mercury most (4.0 corresponds to Juputer)(causes the largest change):

<center>Fig 4. precession changes as adding planet to the system</center>

![image-20221118071531396](Report%20on%20The%20Mighty%20Big%20Problem.assets/image-20221118071531396.png)



### Part C

Adding a term to the original formula is not hard. Just modify the stepping method is okay.

By taking 20~100 times larger alpha and plot it, we can find that they are proportional. hence take $f(1)$ from the fitting line, we can get the exact real precession. 

<center>Fig 4. Fitting line of alpha and precessions</center>

![image-20221118070608639](Report%20on%20The%20Mighty%20Big%20Problem.assets/image-20221118070608639.png)

To track the perihelion, we plotted mercury-sun-distance-time graph and tried to find all the valley point, which are corresponding to he perihelion. By calculating the angle between two adjacent perihelion vectors, we can get the precession.

The graph is like below:

<center>Fig 5. Example of mercury-sun-distance-time graph and valley markers</center>

![image-20221118071235014](Report%20on%20The%20Mighty%20Big%20Problem.assets/image-20221118071235014.png)

  

