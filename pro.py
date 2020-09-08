#Importing libraries
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import datetime
import pandas as pd
import numpy as np

#Read csv files into a pandas dataframe
#df = pd.read_csv("/Users/aniketsingh/SeniorProject/site_weather.csv")


#Making a list of missing values types
missingValues = ["n/a", "na", " ", "__"]
df = pd.read_csv("site_weather.csv", na_values = missingValues)

df.rename(columns = {'Unnamed: 0': 'Date_And_Time'}, inplace = True)
#First few rows
print(df.head())



#Total missing values for each feature
print("-------------Here are the missing values----------")
print(df.isnull().sum())
sns.lineplot(x="Date_And_Time", y="air_temp_set_1", data=df[0:200])

df['Date_And_Time'] = pd.to_datetime(df['Date_And_Time'])
df['date'] = df['Date_And_Time'].dt.date
print("-------------Here are the dates----------")

print(df['date'])

df['year'] = df['Date_And_Time'].dt.year
df['month'] = df['Date_And_Time'].dt.month
df['day'] = df['Date_And_Time'].dt.day
print("-------------Here are the year----------")
print(df['year'])
