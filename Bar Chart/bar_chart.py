from matplotlib import pyplot as plt 
from collections import Counter
import numpy  as np 
import pandas as pd
import csv


# --------------------------------- 1. Ploting the bar chart -------------------------------------

# print(plt.style.available)
plt.style.use('ggplot')


roll_x  = [ 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36 ]
roll_x_evenly_spaced = np.arange(len(roll_x))
marks_y = [ 35978, 37443, 39876, 43999, 46998, 52840, 55342, 59000, 60543, 62678, 71666, 74939, 75999, 78444 ]

width = 0.2

# plt.plot(roll_x, marks_y, color="#567342", marker="o", label="Student Data")
plt.bar(roll_x_evenly_spaced - width, marks_y, width=width, color="#ff0000", label="Student Data")

# -------------------------------------------------------------------------------------

rank_y = [35999, 37100, 39150, 44678, 47834, 51333, 55200, 58992, 60800, 62500, 70111, 74060, 76889, 80456]

plt.bar(roll_x_evenly_spaced, rank_y, width=width, color="#284051", label="Student Rank")

# You can specify a rotation for the tick
plt.xticks(ticks=roll_x_evenly_spaced, labels=roll_x)

# x axis label
plt.xlabel("Roll Number")
# y axis label
plt.ylabel("Marks")
# Chart Title 
plt.title("Students Marks Chart")
plt.legend()

plt.show() 

# ------------------------ 2. Ploting the bar chart from taking the data from csv file using csv module ----------------------

# Reading csv file
with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	language_counter = Counter()
	# # csv_reader is an iterator so we can access a single row by next method
	# one_row = next(csv_reader)
	# print(one_row['LanguagesWorkedWith'].split(';'))

	for row in csv_reader:
		language_counter.update(row['LanguagesWorkedWith'].split(';'))

	# most_common function returns top 10 most common as list of tuples like ('JavaScript', 59219), ('HTML/CSS', 55466), ('SQL', 47544) 
	# print(language_counter.most_common(10))
	language_data = language_counter.most_common(10)


	languages = []
	rankings  = []

	for data in language_data:
		languages.append(data[0])
		rankings.append(data[1])

	languages.reverse()
	rankings.reverse()

	# # Creating the bar chart
	# plt.bar(languages, rankings)
	# # Setting the plot title 
	# plt.title("Languages Rankings")
	# # Setting the x label
	# plt.xlabel("Programming Languages")
	# # Setting the y label
	# plt.ylabel("Rankings")

	# Creating the horizontal( x-axis will become y and y-axis will become x) bar chart
	plt.barh(languages, rankings)
	# Setting the plot title 
	plt.title("Languages Rankings")
	# Setting the x label
	plt.xlabel("Rankings")
	# Setting the y label
	plt.ylabel("Programming Languages")

	plt.tight_layout()

	# Showing the bar chart
	plt.show()

# ------------------------ 3. Ploting the bar chart from taking the data from csv file using pandas module ----------------------


# Reading csv file by creating the pandas dataframe
csv_data = pd.read_csv('data.csv')
language_data = csv_data['LanguagesWorkedWith']



language_counter = Counter()
# # csv_reader is an iterator so we can access a single row by next method
# one_row = next(csv_reader)
# print(one_row['LanguagesWorkedWith'].split(';'))

for row in language_data:
	language_counter.update(row.split(';'))

# most_common function returns top 10 most common as list of tuples like ('JavaScript', 59219), ('HTML/CSS', 55466), ('SQL', 47544) 
# print(language_counter.most_common(10))
language_data = language_counter.most_common(10)


languages = []
rankings  = []

for data in language_data:
	languages.append(data[0])
	rankings.append(data[1])

languages.reverse()
rankings.reverse()

# # Creating the bar chart
# plt.bar(languages, rankings)
# # Setting the plot title 
# plt.title("Languages Rankings")
# # Setting the x label
# plt.xlabel("Programming Languages")
# # Setting the y label
# plt.ylabel("Rankings")

# Creating the horizontal( x-axis will become y and y-axis will become x) bar chart
plt.barh(languages, rankings)
# Setting the plot title 
plt.title("Languages Rankings")
# Setting the x label
plt.xlabel("Rankings")
# Setting the y label
plt.ylabel("Programming Languages")

plt.tight_layout()

# Showing the bar chart
plt.show()




