from matplotlib import pyplot as plt 


chart_data  = [180, 240, 320, 60, 400]
labels      = ['Fair','Average', 'good', 'poor', 'Excellent']
colors      = ['yellow', 'blue', 'orange', 'red', 'green']
colors_code = ['#FFFF00', '#0000FF', '#FFA500', '#FF0000', '#00FF00']
# Explode that section out of circle
explode     = [0,0,0,0,0.1] 

plt.pie(chart_data, labels=labels, colors=colors_code, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

# Setting the plot title 
plt.title("Student Grades")

plt.show()