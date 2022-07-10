from matplotlib import pyplot as plt 

plt.style.use('ggplot')


minutes = [1,2,3,4,5,6,7,8,9]

player1 = [1, 2, 2, 2, 5, 6, 6, 8, 9]
player2 = [1, 1, 1, 3, 4, 5, 5, 5, 5]
player3 = [1, 2, 3, 3, 3, 3, 3, 3, 4]

labels = ['Player 1', 'Player 2', 'Player 3']
colors = ['#FFA500', '#FF0000', '#00FF00']

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc='upper left')

plt.title("Players score chart")
plt.tight_layout()
plt.show()