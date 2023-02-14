# Project 3 Report

## Question 1

We used `unique` method to find all distinct values of Origin column and Units column.

```Matlab
data = readtable("bananas.csv")
ori = unique(data.Origin);
units = unique(data.Units);
```

And we got the following results:

```
Distinct Origins:
    {'acp_bananas'       }                  
    {'all_bananas'       }
    {'belize'            }
    {'brazil'            }
    {'cameroon'          }
    {'colombia'          }
    {'costa_rica'        }
    {'dollar_bananas'    }
    {'dominican_republic'}
    {'ecuador'           }
    {'eu'                }
    {'eu_bananas'        }
    {'ghana'             }
    {'guadeloupe'        }
    {'guatemala'         }
    {'honduras'          }
    {'ivory_coast'       }
    {'jamaica'           }
    {'malaysia'          }
    {'martinique'        }
    {'mexico'            }
    {'nicaragua'         }
    {'panama'            }
    {'somalia'           }
    {'st_vincent'        }
    {'surinam'           }
    {'venezuela'         }
    {'windward_isles'    }
Count: 28
Distinct Units:
      {'｣/kg'}
Count 1
```

## Question 2

We used `grpstats` method to find the mean price from different origins:

```matlab
origin_group = grpstats(data, "Origin", "mean", "DataVars", "Price");
mean_prices = origin_group(:, ["mean_Price"])
```

And we got the following results:

                              mean_Price
                              __________
    
        costa_rica             0.74284  
        guatemala              0.66719  
        dollar_bananas         0.68709  
        all_bananas            0.73941  
        colombia               0.73633  
        dominican_republic     0.63701  
        acp_bananas            0.62421  
        belize                 0.70425  
        panama                 0.76091  
        ivory_coast            0.64778  
        cameroon                0.6698  
        honduras               0.68532  
        ghana                   0.6399  
        ecuador                0.69899  
        guadeloupe             0.56162  
        eu                        0.86  
        brazil                 0.62292  
        nicaragua              0.60542  
        mexico                 0.64567  
        windward_isles         0.54596  
        jamaica                0.60061  
        st_vincent             0.44149  
        surinam                0.59271  
        eu_bananas             0.53265  
        martinique             0.57364  
        venezuela              0.52092  
        somalia                   0.74  
        malaysia               0.59333  
## Question 3

We used `boxplot` to do the plotting and used logical array to check if the origin is in the origin array we are interested in.

```matlab
pool = [
    "colombia"
    "costa_rica"
    "dominican_republic"
    "honduras"
    "jamaica"
    "windward_isles"
    "mexico"
];

inpool = @(x) sum(x == pool) > 0;
idxs = [];
for i = 1 : length(data.Origin)
    if sum(inpool(data.Origin(i))) > 0 % the origin is in the array 'pool'
        idxs = [idxs;i];
    end
end

selected = data(idxs, ["Origin", "Price"]) % filter rows with origin in the array
figure;
boxplot(selected.Price, selected.Origin) % plot
title("Boxplot of prices of some origins")
xlabel("Origin")
ylabel("Price")
```

And we got the following results:

![image-20221125223742385](C:%5CUsers%5C35995%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20221125223742385.png)

The plotting graph gives us the following information:

- prices distribution of Costa Rica origin are nearly the same;
- prices of the goods of Costa Rica, Columbia, Dominican Republic have occasions that fluctuate largely;
- prices of the goods of Jamaica fluctuate the less;
- the goods from Windward Isles once reaches the lowest bound.

## Question 4

We plotted the fluctuation graph of the prices of Colombia goods:

```matlab
context = groups{6};
ts = table2array(context(:, 1));
ys = table2array(context(:, 2));

colors = [
    [255, 131, 123] / 255;
    [160, 231, 103] / 255;
    [116, 203, 241] / 255;
    [201, 141, 233] / 255;
    [255, 169, 123] / 255;
    [253, 244, 152] / 255
];

figure;
for i = 1 : length(ts) - 1
    t = month(ts(i));
    if t < 2 || t > 10
        c = colors(1, :);
    elseif t < 5
        c = colors(2, :);
    elseif t < 8
        c = colors(3, :);
    else
        c = colors(4, :);
    end
    plot(ts(i:i+1), ys(i:i+1), "Color", c);
    if i == 1
        hold on 
    end
end
title("Seasonal price")
xlabel("Time")
ylabel("Price")
hold off
```



![image-20221125235525294](Report%20on%20Project%203.assets/image-20221125235525294.png)

The graph use

## Question 5

The correlation coefficient is defined as 

$r_{xy}=\dfrac{\displaystyle\sum_{i=1}^n(x_i-\bar x)(y_i-\bar y)}{\displaystyle\sqrt{\sum_{i=1}^n (x_i-\bar{x})^2}\sqrt{\sum_{i=1}^n (y_i-\bar y)^2}}$

and matlab provides `corrcoef` method to calculate this

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