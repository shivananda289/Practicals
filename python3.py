#create a python program to display graphs

import matplotlib.pyplot as plt
x = ['A', 'B', 'C']
y = [10, 5, 8]
colors_bar = ['red', 'green', 'blue'] 
plt.bar(x, y, color=colors_bar)
plt.title("Bar Chart")
plt.show()
x_scatter = [1, 2, 3, 4]
y_scatter = [2, 4, 6, 8]
plt.scatter(x_scatter, y_scatter, color='purple')
plt.title("Scatter Plot")
plt.show()
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color='orange')
plt.title("Histogram")
plt.show()
labels = ['Apples', 'Bananas', 'Cherries']
sizes = [30, 45, 25]
colors_pie = ['#ff9999', '#66b3ff', '#99ff99']  
plt.pie(sizes, labels=labels, colors=colors_pie, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
