from matplotlib import pyplot as plt 
import pandas as pd

path = 'data.csv'
data = pd.read_csv(path)

age_data        = data['Age']
dev_rank        = data['All_Devs']
python_rank     = data['Python']
javascript_rank = data['JavaScript']  

plt.plot(age_data, dev_rank, linestyle="dotted", label="All developers")
plt.plot(age_data, python_rank, label='Python Developers')

median = 50000

# matplotlib.pyplot.fill_between() is used to fill area between two horizontal curves
# matplotlib.pyplot.fill_between(x, y1, y2=0, where=None, step=None, interpolate=False, *, data=None, **kwargs)\

# plt.fill_between(age_data, python_rank, median, where = (python_rank > median), color='green', interpolate=True, alpha=0.25)
# plt.fill_between(age_data, python_rank, median, where = (python_rank <= median), color='red', interpolate=True, alpha=0.25)


# Filling the area between two lines
plt.fill_between(age_data, python_rank, dev_rank, where = (python_rank > dev_rank), color='green', interpolate=True, alpha=0.25, label="Good")
plt.fill_between(age_data, python_rank, dev_rank, where = (python_rank <= dev_rank), color='red', interpolate=True, alpha=0.25, label='Bad')

plt.legend()

plt.title("Developers ranking")
plt.xlabel("Ages")
plt.ylabel("Ranking")

plt.show()


