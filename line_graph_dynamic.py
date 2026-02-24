import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o')

def update(frame):
    try:
        y = float(input("Enter value: "))
        x_data.append(len(x_data) + 1)
        y_data.append(y)

        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()
    except:
        pass
    return line,

ani = FuncAnimation(fig, update, interval=1000)

plt.xlabel("Input Count")
plt.ylabel("User Value")
plt.title("Dynamic Line Graph")
plt.show()
