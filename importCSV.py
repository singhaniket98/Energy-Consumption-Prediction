#Importing libraries 
import pandas as pd
import numpy as np

#Read csv files into a pandas dataframe 
df = pd.read_csv("site_weather.csv")

#First few rows
print(df.head())