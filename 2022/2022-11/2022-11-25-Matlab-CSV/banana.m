clear all;
clf reset;

% Read in CSV
data = readtable("bananas.csv")

% Filter out unique origin and units
ori = unique(data.Origin);
units = unique(data.Units);

disp("Distinct " + length(ori) + " Origins:")
disp(ori)
disp("Distinct " + length(units) + " Units:")
disp(units)
% Hence there are 28 distinct origins and only 1 unit.

% 2. Mean prices. Aggregation group by Origin
aggr = grpstats(data, "Origin", "mean", "DataVars", "Price")

% 3. Box Plot
keys = { 'colombia', ...
    'costa_rica', ...
    'dominican_republic', ...
    'honduras',...
    'jamaica',...
    'windward_isles',...
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

% 4. Time Series of Colombia
colombia_indexes = all_origins == 'colombia';

dates = data.Date(colombia_indexes);
pris = data.Price(colombia_indexes);

fig = figure;
for i = 1 : length(dates) - 1
    m = month(dates(i));
    if m < 2 || m > 10
        color = 'red';
    elseif m < 5
        color = 'green';
    elseif m < 8
        color = 'blue';
    else
        color = 'yellow';
    end
    plot(dates(i:i+1), pris(i:i+1), "Color", color);
    if i == 1
        hold on 
    end
end
xlabel("Date")
ylabel("Price")
hold off

% 5. Correlation Coefficients of Colombia and Costa Rica 
costa_rica_indexes = all_origins == 'costa_rica';

dates2 = data.Date(costa_rica_indexes);
pris2 = data.Price(costa_rica_indexes);

uni_times = max(min(datenum(dates2)), min(datenum(dates))) ...
    : min(max(datenum(dates2)), max(datenum(dates)));
uni_times = datetime(uni_times, "ConvertFrom", "datenum");

pris_ = interp1(dates, pris, uni_times, "linear")';
pris2_ = interp1(dates2, pris2, uni_times, "linear")';

disp("Correlation Coefficients:")
corrcoef([pris_ pris2_])


