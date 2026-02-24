import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
sc = ax.scatter(x_data, y_data)

def update(frame):
    try:
        x = float(input("Enter X value: "))
        y = float(input("Enter Y value: "))
        x_data.append(x)
        y_data.append(y)

        ax.clear()
        ax.scatter(x_data, y_data)
        ax.set_xlabel("X Values")
        ax.set_ylabel("Y Values")
        ax.set_title("Dynamic Scatter Plot")
    except:
        pass

ani = FuncAnimation(fig, update, interval=2000)

plt.show()
