import pandas as pd 
from matplotlib import pyplot as plt 
from datetime import datetime, timedelta
from matplotlib import dates as mplt_dates


plt.style.use("ggplot")

# ---------------------------- Program 1 --------------------------------------

# x axis data
dates_x = [
	datetime(2022, 7, 13),
	datetime(2022, 7, 14),
	datetime(2022, 7, 15),
	datetime(2022, 7, 16),
	datetime(2022, 7, 17),
	datetime(2022, 7, 18),
	datetime(2022, 7, 19),
	datetime(2022, 7, 20)
] 

# y axis data
y = [0,2,3,4,6,7,8,9]


# plotting the data
plt.plot_date(dates_x, y, linestyle="solid")


# Formatting the date styles according to x axis
# gcp = 'Get current format' , autofmt = 'auto format'. It will rotate the dates according to x axis
plt.gcf().autofmt_xdate()


# Formatting the date according to x axis
date_format = mplt_dates.DateFormatter("%d-%b-%Y")
# gca = 'get current axis'
plt.gca().xaxis.set_major_formatter(date_format)


plt.tight_layout()
plt.show()

# ---------------------------- Program 2 --------------------------------------

# Reading data from csv file
path = 'data.csv'
df   = pd.read_csv(path)

# Convert date string to date and then sorting
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

date_x        = df['Date']
opening_price = df['Open']

# Plotting the data
plt.plot_date(date_x, opening_price, linestyle="solid")

# Formatting the date styles 
plt.gcf().autofmt_xdate()


plt.tight_layout()
plt.show() 