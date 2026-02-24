import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, (ax1, ax2) = plt.subplots(1, 2)

def update(frame):
    try:
        x = float(input("Enter X value: "))
        y = float(input("Enter Y value: "))
        x_data.append(x)
        y_data.append(y)

        ax1.clear()
        ax1.plot(x_data, y_data, marker='o')
        ax1.set_title("Line Chart")

        ax2.clear()
        ax2.scatter(x_data, y_data)
        ax2.set_title("Scatter Chart")
    except:
        pass

ani = FuncAnimation(fig, update, interval=2000)

plt.tight_layout()
plt.show()
