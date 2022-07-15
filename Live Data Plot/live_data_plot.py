from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count
import random 


plt.style.use('ggplot')

# # -------------- 1. Plotting a simple line chart ------------------
# values_x = [0,1,3,5,7,9,10]
# values_y = [0,1,4,5,6,7,8]
# plt.plot(values_x, values_y)

# ------------------2. Plotting the live data plot by creating a function -------------------------

# values_x = []
# values_y = []

# index = count()

# # Here i parameter is interval
# def frequent_values(i):
# 	values_x.append(next(index))
# 	values_y.append(random.randint(0,7))

# 	# cla = clear axis : to use same color line when each time plot creates 
# 	plt.cla()
# 	plt.plot(values_x, values_y)

# # Here 1000 in miliseconds(1000ms = 1 second) 
# animation = FuncAnimation(plt.gcf(), frequent_values, interval=1000) 

# ------------------- 3. Plotting the live data plot by supplying the regular data by csv file --------- 

def frequent_values(i):
	df       = pd.read_csv('data.csv')
	value_x  = df['value_x']
	value_y1 = df['count1']
	value_y2 = df['count2']

	plt.cla()
	plt.plot(value_x, value_y1, label='Stream 1')
	plt.plot(value_x, value_y2, label='Stream 2')

	plt.legend(loc='upper left')


animation = FuncAnimation(plt.gcf(), frequent_values, interval=1000) 


plt.tight_layout()
plt.show()