import pandas as pd
import matplotlib.pyplot as plt
from pandas import Grouper, DataFrame, read_csv
from matplotlib import pyplot

# Read the time series dataset
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True)

# Display first five rows
print(series.head())

# Line plot
series.plot()
plt.title("Line Plot of Daily Minimum Temperatures")
pyplot.show()

# Dot style line plot
series.plot(style='k.')
plt.title("Dot Plot of Daily Minimum Temperatures")
pyplot.show()

# Histogram
series.hist()
plt.title("Histogram of Daily Minimum Temperatures")
pyplot.show()

# Boxplot grouped by year
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
    years[name.year] = group.values
years.boxplot()
plt.title("Boxplot of Daily Minimum Temperatures by Year")
pyplot.show()
