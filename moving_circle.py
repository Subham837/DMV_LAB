import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as animation
import numpy as np

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
circle = patches.Circle((1, 5), 0.5, fc='blue')
ax.add_patch(circle)

def animate(i):
    circle.center = (i * 0.1, 5)
    return circle,

ani = animation.FuncAnimation(fig, animate, frames=80, interval=20, blit=True)
plt.show()
