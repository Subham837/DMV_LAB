import matplotlib.pyplot as plt

data = [30, 25, 20, 15, 10]
labels = ['A', 'B', 'C', 'D', 'E']

plt.pie(data, labels=labels, autopct='%1.1f%%')
plt.title('Static Pie Chart')
plt.show()
