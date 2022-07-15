from matplotlib import pyplot as plt 
import pandas as pd

print(plt.style.available)
plt.style.use('ggplot')

x_values = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y_values = [99,86,87,88,111,86,103,87,94,78,77,85,86]
 
# c for colors list, s for dot sizes 
# plt.scatter(x_values, y_values, s=10, c="red", marker="x")

# ----- Using the color list--------
colors   = ["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"]
# plt.scatter(x_values, y_values, s=10, c=colors, marker="x")
plt.scatter(x_values, y_values, c=colors, edgecolor="black", alpha=0.75, linewidth=1)


# # ----- Using the color map(cmap) --------
# colors   = [7,5,4,6,8,3,10,9,1,2,7,4,9]
# plt.scatter(x_values, y_values, c=colors, cmap="winter")

# # ----- Setting the color bar --------
# cbar   = plt.colorbar()
# cbar.set_label('Color Range') 
# colors = [7,5,4,6,8,3,10,9,1,2,7,4,9]
# plt.scatter(x_values, y_values, c=colors, cmap="winter")

# ---------  Reading the data from csv file ---------
path = "row_data.csv"
df = pd.read_csv(path)

view_counts        = df['view_counts']
likes              = df['likes']
like_dislike_ratio = df['like_dislike_ratio']

cbar = plt.colorbar()
cbar.set_label("Color Range")

plt.scatter(view_counts, likes, c=like_dislike_ratio, cmap='terrain', edgecolor="black", linewidth=1, alpha=0.50)

plt.xscale('log')
plt.yscale('log')

plt.title("Post records")
plt.xlabel('Total Counts')
plt.ylabel('Total Likes')

plt.tight_layout()
plt.show()