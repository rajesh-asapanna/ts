# load
from pandas import read_csv
series = read_csv('daily-total-female-births.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
print(type(series))
# print(series.head(10))
# print(series.size)
# print(series['1959-01'])
print(series.describe())