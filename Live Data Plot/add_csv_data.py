#  ----- Program to continuously add data to csv file ------

import random
import time
import csv

value_x = 0
count1  = 500
count2  = 500

header_data = ['value_x', 'count1', 'count2']

# Writing the header data to csv file
with open('data.csv', 'w') as csv_file:
	csv_writer = csv.DictWriter(csv_file, fieldnames = header_data)
	csv_writer.writeheader()


# Adding data to existing csv file
while True:

	with open('data.csv', 'a') as csv_file:
		csv_writer = csv.DictWriter(csv_file, fieldnames=header_data)

		# Creating raw data to insert
		insert_data = {
			'value_x': value_x,
			'count1': count1,
			'count2': count2
		}

		# Writing data to csv file
		csv_writer.writerow(insert_data)
		print(value_x, count1, count2)

		value_x += 1
		count1  =  count1 + random.randint(-5, 5)
		count2  =  count2 + random.randint(-7, 7)

	time.sleep(1)





