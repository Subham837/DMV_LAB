import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

labels = []
sizes = []

fig, ax = plt.subplots()

def update(frame):
    try:
        label = input("Enter label: ")
        value = float(input("Enter value: "))
        labels.append(label)
        sizes.append(value)

        ax.clear()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%')
        ax.set_title("Dynamic Pie Chart")
    except:
        pass

ani = FuncAnimation(fig, update, interval=2000)

plt.show()
