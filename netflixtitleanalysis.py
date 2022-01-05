import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

df = pd.read_csv("netflix_titles.csv")
print(df)

#drop columns Type, Director, Country, Date Added, Duration, Description and Rating.
#Might include Description in a future edit for sentiment analysis
df.drop(columns = ["type", "director", "country", "date_added", "duration", "description", "rating"], axis = 1, inplace = True)

#drop rows with NaN cast 
df.dropna(axis = 0, inplace = True)

#extract all genres in the "Listed In" column into a list for plotting
df = df.join(df["listed_in"].str.split(", ", expand = True).rename(columns = {0: "Genre 1", 1: "Genre 2", 2: "Genre 3"}))
col_values = df[["Genre 1", "Genre 2", "Genre 3"]].values.ravel()
unique_values = pd.unique(col_values)
unique_lst = list(filter(lambda v: v, unique_values.tolist()))
len(unique_lst)



