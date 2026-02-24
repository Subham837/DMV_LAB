import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

labels = []
values = []

fig, ax = plt.subplots()

def update(frame):
    try:
        label = input("Enter label: ")
        value = float(input("Enter value: "))
        labels.append(label)
        values.append(value)

        ax.clear()
        ax.bar(labels, values, color="skyblue")
        ax.set_xlabel("Categories")
        ax.set_ylabel("Values")
        ax.set_title("Dynamic Bar Chart")
    except:
        pass

ani = FuncAnimation(fig, update, interval=2000)

plt.show()
