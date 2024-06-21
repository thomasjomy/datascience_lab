import matplotlib.pyplot as plt

data = [1, 2, 3, 4]
explode_values = (0.1, 0.1, 0.1, 0.1)
plt.pie(data, explode=explode_values)
plt.title("Pie chart")
plt.show()
