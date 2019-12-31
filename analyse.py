#!/usr/bin/env python3

import pandas
import matplotlib.pyplot as plt
import datetime

df = pandas.read_csv("pingstats",sep=" ",header=None,usecols=[0,7],names=["Time","Ping"])

start_time = df.iloc[0][0]
print("start_time=",start_time)

df.Time = pandas.to_datetime(df.Time,unit='s')
#df['Time'] = df['Time'] - int(start_time)

quantiles = []
y = []

for i in range(0,100):
    print(i,df.quantile(float(i)/100.0)[0])
    y.append(i)
    quantiles.append(df.quantile(float(i)/100.0)[0])


fig, ax = plt.subplots()
n, bins, patches = ax.hist(quantiles, 99)

print(df.describe())
ax.plot(bins,y)
ax.set_xlabel("Ping time (ms)")
ax.set_ylabel("Density")
fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
#df.plot(kind='scatter',x='Time',y='Ping',ax=ax,s=0.25)
df.plot(kind='line',x='Time',y='Ping',ax=ax)
plt.show()
#print(quantiles)