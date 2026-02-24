import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x)
line, = ax.plot(x, y)

def animate(i):
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig, animate, interval=20, blit=True)

plt.show()
