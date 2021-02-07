from pprint import pprint
from pandas import read_csv, DataFrame
series = read_csv( 'daily-min-temperatures.csv' , header=0, index_col=0, parse_dates=True, squeeze=True)


#pprint(list(series.index)[100].month)
df = DataFrame()
#exit()

df['month'] = [series.index[i].month for i in range(len(series))]
df['day'] = [series.index[i].day for i in range(len(series))]
df['temperature'] = [series[i] for i in range(len(series))]
print(df.head(5))
print(series.head(10))