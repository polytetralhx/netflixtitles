import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

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
type(df['cast'].values[2])


#add a genre dictionary. for every genre add cast: count into a actor dictionary
genred = {}
for i in df.index:
    for actor in df["cast"][i].split(", "):
        if df["Genre 1"][i]:
            if df["Genre 1"][i] not in genred:
                genred[df["Genre 1"][i]] = {}
            actord = genred[df["Genre 1"][i]]
            if actor not in actord:
                actord[actor] = 0
            actord[actor] += 1
        if df["Genre 2"][i]:
            if df["Genre 2"][i] not in genred:
                genred[df["Genre 2"][i]] = {}
            actord = genred[df["Genre 2"][i]]
            if actor not in actord:
                actord[actor] = 0
            actord[actor] += 1
        if df["Genre 3"][i]:
            if df["Genre 3"][i] not in genred:
                genred[df["Genre 3"][i]] = {}
            actord = genred[df["Genre 3"][i]]
            if actor not in actord:
                actord[actor] = 0
            actord[actor] += 1

#find most frequent cast for every genre. 
res = "Cast with highest frequency in each genre:"
for genre, actors in genred.items():
    maxactor = max(actors, key = actors.get)
    maxfreq = genred[genre][maxactor]
    res += f"\n{genre}: {maxactor} ({maxfreq} appearance(s))"
print(res)
