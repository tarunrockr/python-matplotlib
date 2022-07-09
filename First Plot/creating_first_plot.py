from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1  

x_ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

y_axis = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# Passing x axis and y axis data to 1st graph in plot function
# Adding 'java' legend to plot using label
# color="#444444" it can be 
plt.plot(x_ages, y_axis, color='k', linestyle='--', marker='o', label='Java')

y_ages_final =  [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

# Passing x axis and y axis data to 2nd graph in plot function
# Adding 'python' legend to plot using label
plt.plot(x_ages, y_ages_final, color='b', marker='.', linewidth='3', label="Python")

# x axis label
plt.xlabel('Age Group')
# y axis label 
plt.ylabel('Monthly salary')
# Graph title
plt.title("Monthly salary (INR) by Age Group")

# # Adding the plot name(legend) in the order of adding plot sequence
# plt.legend(['First Group','Second Group'])
# If we are passing legend using label tag then need to call legend function without argument
plt.legend()

# The tight_layout() function in pyplot module of matplotlib library is used to automatically adjust subplot parameters to give specified padding.
plt.tight_layout()

# Formatting [marker][line][color]

# displaying the data using show function
#plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# x_ages = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
#           36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

# y_axis = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
#             84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

# # using available styles
# plt.style.use('fivethirtyeight')
# #print(plt.style.available)
# plt.plot(x_ages, y_axis)
# plt.show()


# # ------------------- Use of xkcd --------------------------
with plt.xkcd():
    plt.plot([1, 2, 3, 4], [5, 4, 9, 2])
    plt.title('matplotlib.pyplot.xkcd()')
    plt.axhline(y = 0, color ='k')

# --------------------- Saving the graph as image in system ----------
path = 'grph.png' # Storing in the same directory
plt.savefig(path)
plt.show()
   
