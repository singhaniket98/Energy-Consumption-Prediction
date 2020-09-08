import pandas as pd

print(pd.__version__)

df = pd.read_csv(r'../data/site_weather.csv')
print(df)


