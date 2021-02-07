import time
from pandas import read_csv, DataFrame, concat

series = read_csv( 'daily-min-temperatures.csv' , header=0, index_col=0, parse_dates=True, squeeze=True)

temps = DataFrame(series.values)

# print('before shift:')
# print(temps)

shifted = temps.shift(1)

# print('before rollw:')
# print(shifted)

window = shifted.rolling(window=2)

# print('finally:')
# for cnt, i in enumerate(window):
#     if cnt > 3640:
#         print(i)
#         time.sleep(1)

means = window.mean()
df = concat([means, temps], axis=1)
df.columns = ['mean(t-1,t)', 't+1']
print(df.head())

temps1 = DataFrame(series.values)
width = 3
shifted1 = temps1.shift(width-1)
window1 = shifted.rolling(window=width)
df1 = concat([window1.min(), window1.mean(), window1.max(), temps1], axis=1)
df1.columns = ['min', 'mean', 'max', 't+1']
print(df1.head(10))