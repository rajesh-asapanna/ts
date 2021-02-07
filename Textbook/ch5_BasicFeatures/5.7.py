from pandas import read_csv, DataFrame, concat

series = read_csv( 'daily-min-temperatures.csv' , header=0, index_col=0, parse_dates=True, squeeze=True)

## expanding stats

temps = DataFrame(series.values)
window = temps.expanding()

# for cnt, i in enumerate(window):
#     if cnt<10: 
#         print(i)

df = concat([window.min(), window.mean(), window.max(), temps.shift(-1)], axis=1)
df.columns = [ ' min ' , ' mean ' , ' max ' , ' t+1 ' ]
print(df.head(5))