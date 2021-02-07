from pandas import read_csv, DataFrame, concat
from pprint import pprint
series = read_csv( 'daily-min-temperatures.csv' , header=0, index_col=0, parse_dates=True, squeeze=True)

temps = DataFrame(series.values)
# print(series.index)

df = concat([temps.shift(2), temps.shift(1), temps], axis=1)
df.columns = ['t-1', 't', 't+1']
print(df.head())