import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]


fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

plt.show()
