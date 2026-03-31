import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation

# Initial position and velocity
x, y = 0, 0
dx, dy = 0, 0

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

circle = Circle((x, y), 0.5, color='blue')
ax.add_patch(circle)

# Key press event
def on_key(event):
    global dx, dy
    
    if event.key == 'up':
        dy = 0.2
    elif event.key == 'down':
        dy = -0.2
    elif event.key == 'left':
        dx = -0.2
    elif event.key == 'right':
        dx = 0.2

# Key release (stop movement)
def on_key_release(event):
    global dx, dy
    
    if event.key in ['up', 'down']:
        dy = 0
    if event.key in ['left', 'right']:
        dx = 0

# Animation update function
def update(frame):
    global x, y
    
    x += dx
    y += dy
    
    # Boundary check
    if x > 10: x = 10
    if x < -10: x = -10
    if y > 10: y = 10
    if y < -10: y = -10
    
    circle.center = (x, y)
    return circle,

# Connect events
fig.canvas.mpl_connect('key_press_event', on_key)
fig.canvas.mpl_connect('key_release_event', on_key_release)

ani = FuncAnimation(fig, update, frames=200, interval=20)

plt.title("Use Arrow Keys to Move the Circle")
plt.grid()
plt.show()
