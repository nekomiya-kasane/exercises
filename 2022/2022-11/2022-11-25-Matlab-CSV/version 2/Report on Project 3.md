# Report on Project 3

<center>
    10767474
</center>

## Question 1

*This question is to find all distinct entries under the Origin and Units headers.*

### Method

Matlab provides `unique` method to extract distinct values of a column:

```matlab
data = readtable("bananas.csv")
ori = unique(data.Origin);
units = unique(data.Units);
```

which outputs

```text
28 distinct origins:                 1 distinct unit:
{'acp_bananas' }                     {'｣/kg'}
{'all_bananas' }
{'belize' } 
{'brazil' }
{'cameroon' }
{'colombia' }
{'costa_rica' }
{'dollar_bananas' }
{'dominican_republic'}
{'ecuador' }
{'eu' }
{'eu_bananas' }
{'ghana' }
{'guadeloupe' }
{'guatemala' }
{'honduras' }
{'ivory_coast' }
{'jamaica' }
{'malaysia' }
{'martinique' }
{'mexico' }
{'nicaragua' }
{'panama' }
{'somalia' }
{'st_vincent' }
{'surinam' }
{'venezuela' }
{'windward_isles' }
```

Hence, we can find that there are 28 distinct origins producing bananas and one distinct unit which is ‘£/kg’ by the Matlab `unique` method.

## Question 2

Numerous reasons will cause significant fluctuations in the price of bananas. In this situation, we must figure out the average price of each different variety of banana across all origins.

### Method

Matlab provides `grpstats` method to get some aggregation statistical values 

of a table:

```matlab
aggr = grpstats(data, "Origin", "mean", "DataVars", "Price")
```

### Result:

```text
             Origin              GroupCount mean_Price
             ___________________ __________ __________
 costa_rica     {'costa_rica' }   1144      0.74284
 guatemala      {'guatemala' }    360       0.66719
 dollar_bananas {'dollar_bananas' }  1249   0.68709
 all_bananas    {'all_bananas' }  646       0.73941
 colombia       {'colombia' }     1085      0.73633
 dominican_republic {'dominican_republic'}  763 0.63701
 acp_bananas    {'acp_bananas' }  1171      0.62421
 belize         {'belize' }       386       0.70425
 panama         {'panama' }       651       0.76091
 ivory_coast    {'ivory_coast' }  406       0.64778
 cameroon       {'cameroon' }     683       0.6698
 honduras       {'honduras' }     190       0.68532
 ghana          {'ghana' }        102       0.6399
 ecuador        {'ecuador' }      1000      0.69899
 guadeloupe     {'guadeloupe' }   278       0.56162
 eu             {'eu' }           2         0.86
 brazil         {'brazil' }       445       0.62292
 nicaragua      {'nicaragua' }    24        0.60542
 mexico         {'mexico' }       127       0.64567
 windward_isles {'windward_isles' }  673    0.54596
 jamaica        {'jamaica' }      99        0.60061
 st_vincent     {'st_vincent' }   47        0.44149
 surinam        {'surinam' }      255       0.59271
 eu_bananas     {'eu_bananas' }   378       0.53265
 martinique     {'martinique' }   253       0.57364
 venezuela      {'venezuela' }    109       0.52092
 somalia        {'somalia' }      2         0.74
 malaysia       {'malaysia' }     3         0.59333
```

## Question 3

*This question is to do a grouped box plot comparing the variation of the prices of the different varieties of bananas with the given Origins.*

### Method

We used a key map to filter given origins:

- firstly, we create a map which takes the requested origins as keys, and some integers as values (values not used indeed)
- secondly, we traverse all rows in the table, and make use of Matlab’s `isKey` method to determine whether the origin of a row is in the given origins.
- if the origin is in the given origins, we collect the price and origin of this row into lists `prices` and `origins`
- finally, call Matlab’s `boxplot` function with `prices` and `origins` to plot a box graph.

```matlab
keys = { 'colombia', 
	'costa_rica', 
	'dominican_republic', 
	'honduras', 
	'jamaica', 
	'windward_isles', 
	'mexico'
};
values = 1 : length(keys);
map_index = containers.Map(keys, values);

prices = [];
origins = [];
all_origins = [];

for i = 1 : length(data.Origin) % for each row of the table
	this_origin = data.Origin(i);
	this_origin = this_origin{1};
	all_origins = [all_origins; convertCharsToStrings(this_origin)];
	if ~isKey(map_index, this_origin) % not in keys
		continue;
	end
	prices = [prices; data.Price(i)]; % collect prices and origins
	origins = [origins; convertCharsToStrings(this_origin)];
end

figure;
boxplot(prices, origins);
xlabel("Origin")
ylabel("Price")
```

And the result graph is like this

![1670803386091](Report on Project 3.assets\1670803386091.png)

From the graph we can see that: 

> Compared to Jamaica variations more stable than others republic experiences a significant fluctuation in banana's price. Moreover, it is the best way to buy banana in Windward isles, which got the lowest price for banana. in addition, we can get the similar price in Costa and Colombia.

## Question 4

*This question is to find any seasonal trends of the time series for the variety with Origin ‘colombia’.*

### Method

We plotted the fluctuation graph of the prices in Colombia by months:

for every date interval between adjacent rows containing the origin “Colombia” (already sorted by date), we check the month of the starting date

- if the month is among November, December and January, plot it red
- if the month is among February, March and April, plot it green
- if the month is among May, June and July, plot it blue
- otherwise, plot the line segment yellow

```matlab
colombia_indexes = all_origins ҧ 'colombia';

dates = data.Date(colombia_indexes);
pris = data.Price(colombia_indexes);

fig = figure;
for i = 1 : length(dates) - 1
	m = month(dates(i));
	if m < 2 җ m > 10 % winter
		color = 'red';
	elseif m < 5 % spring
		color = 'green';
	elseif m < 8 % summer
		color = 'blue';
	else % autumn
		color = 'yellow';
	end
	plot(dates(i:i+1), pris(i:i+1), "Color", color);
	if i ҧ 1
		hold on
	end
end
xlabel("Date")
ylabel("Price")
hold off
```

![1670803476210](Report on Project 3.assets\1670803476210.png)

In this graph, red stands for winter, green for spring, blue for summer, yellow for autumn. We can clearly see the seasonal change with this coloring: 

> The temperature is the key determinant that influences the banana's price in Colombia which can be seen clearly in the line diagram. Generally speaking, there exist a significant fluctuation in Colombia banana's price during four seasons. It's because of the extreme temperature fluctuations   between spring and summer and winter and autumn that causes the variation. For, example the price arrive its lowest point which is £0.4/kg in 2010 during winter and spring but in nearly 2008's spring, the banana’s price reaches peak is almost £1.3/kg. Furthermore, banana's price got almost £0.4/kg in 2020 spring and autumn. These facts demonstrate that the temperature will influence the price of bananas in Colombia.

## Question 5

*This question is to calculate the correlation coefficient of 2 discreate time series, which are obtained from the variety with Origin ‘colombia’ and ‘costa_rica’.*

### Method

The correlation coefficient is defined as 

$r_{xy}=\dfrac{\displaystyle\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\displaystyle\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2}\sqrt{\sum_{i=1}^n (y_i-\bar y)^2}}$

and matlab provides `corrcoef` method to calculate this.

But here is a problem, the number of the sample points of Colombia and Costa Rica is not identical, hence we must do interpolation on the two sets of sample points, and resample two list of data points from the interpolating curves.

The interpolation is done from the earliest date to the latest date.

After interpolating, we get to be able to call `corrcoef` to calculate the correlation coefficient.

```matlab
costa_rica_indexes = all_origins == 'costa_rica';

dates2 = data.Date(costa_rica_indexes);
pris2 = data.Price(costa_rica_indexes);

% since the dimension of the data is not the same, we have to do interpolation on time
uni_times = max(min(datenum(dates2)), min(datenum(dates))) ... 
    : min(max(datenum(dates2)), max(datenum(dates)));
uni_times = datetime(uni_times, "ConvertFrom", "datenum");

pris_ = interp1(dates, pris, uni_times, "linear")';
pris2_ = interp1(dates2, pris2, uni_times, "linear")';

disp("Correlation Coefficients:")
corrcoef([pris_ pris2_])
```

which results in $\begin{bmatrix}1&0.7695\\0.7695&1\end{bmatrix}$, indicating that $r=0.7695$.