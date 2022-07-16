from matplotlib import pyplot as plt
import pandas as pd  


plt.style.use('ggplot')

# Reading data from csv file
df = pd.read_csv('data.csv')

ages_x           = df['Age']
all_developers_y = df['All_Devs']
python_y         = df['Python']
php_y            = df['PHP']

# -----------   1. Program for default plot -------------------

# # Plotting all developers 
# plt.plot(ages_x, all_developers_y, label="All Deveploers", linestyle="solid")
# # Plotting python developers 
# plt.plot(ages_x, python_y, label="Python", linestyle="dotted")
# # Plotting php developers 
# plt.plot(ages_x, php_y, label="PHP", linestyle="dashed")

# plt.title("Users with age")
# plt.xlabel("Ages")
# plt.ylabel("Developers")

# -----------   2. Program for line plot using axis -------------------

# figure, axis = plt.subplots()

# # Plotting all developers 
# axis.plot(ages_x, all_developers_y, label="All Deveploers", linestyle="solid")
# # Plotting python developers 
# axis.plot(ages_x, python_y, label="Python", linestyle="dotted")
# # Plotting php developers 
# axis.plot(ages_x, php_y, label="PHP", linestyle="dashed")

# axis.set_title("Users with age")
# axis.set_xlabel("Ages")
# axis.set_ylabel("Developers")

# # -----------   3. Program for line plot using 1 column and 2 axis -------------------

# figure, (axis1, axis2) = plt.subplots(nrows=2, ncols=1, sharex=True)

# # Plotting all developers on axis1
# axis1.plot(ages_x, all_developers_y, label="All Deveploers", linestyle="solid")

# # Plotting python developers on axis2
# axis2.plot(ages_x, python_y, label="Python", linestyle="dotted")
# # Plotting php developers on axis2
# axis2.plot(ages_x, php_y, label="PHP", linestyle="dashed")

# axis1.set_title("Users with age") 
# axis1.set_ylabel("Developers")
# axis1.legend()

# axis2.set_xlabel("Ages")
# axis2.set_ylabel("Developers")
# axis2.legend()

# -----------   4. Program for line plot using 2 figures -------------------

figure1, axis1 = plt.subplots()
figure2, axis2 = plt.subplots()

# Plotting all developers on axis1
axis1.plot(ages_x, all_developers_y, label="All Deveploers", linestyle="solid")

# Plotting python developers on axis2
axis2.plot(ages_x, python_y, label="Python", linestyle="dotted")
# Plotting php developers on axis2
axis2.plot(ages_x, php_y, label="PHP", linestyle="dashed")

axis1.set_title("Users with age") 
axis1.set_ylabel("Developers")
axis1.legend()

axis2.set_xlabel("Ages")
axis2.set_ylabel("Developers")
axis2.legend()


# Saving both figure seperately
# figure1.savefig('Image1.png')
# figure2.savefig('Image2.png')



plt.tight_layout()
plt.show()

