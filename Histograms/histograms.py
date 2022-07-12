from matplotlib import pyplot as plt 
import pandas as pd 

# print(plt.style.available)
plt.style.use('seaborn-deep')

# It is a graph showing the number of observations within each given interval.
# The hist() function in pyplot module of matplotlib library is used to plot a histogram.

# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None, histtype=’bar’, align=’mid’, orientation=’vertical’, rwidth=None, log=False, color=None, label=None, stacked=False, \*, data=None, \*\*kwargs)

#  ----------   1. Without bins parameter ------------
# roll_numbers = [12,12,24,15,18,19,20,20,25,27,34,39,45,46,47]
# plt.hist(roll_numbers, edgecolor='black')

# #  ----------   2. Without bins as a single value ------------
# roll_numbers = [12,12,24,15,18,19,20,20,25,27,34,39,45,46,47]
# plt.hist(roll_numbers, bins=10, edgecolor='black')

# #  ----------   3. Providing the bins value in the form of list ------------
# roll_numbers = [12,12,24,15,18,19,20,20,25,27,34,39,45,46,47]
# bins_values = [10,20,30,40,50] # It will create 4 bins
# plt.hist(roll_numbers, bins=bins_values, edgecolor='black')

path = 'data.csv'
df   = pd.read_csv(path)
ids  = df['id']
ages = df['Age']

bins_values = [10,20,30,40,50,60,70,80,90,100] # It will create 4 bins
plt.hist(ages, bins=bins_values, edgecolor='black')


median_age = 45

# Plotting a vertical line according to x axis
plt.axvline(median_age, color="red", linewidth=1)

plt.title("Student Roll numbers data")
plt.show()
