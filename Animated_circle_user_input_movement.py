import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Initial position
x, y = 0, 0

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

circle = Circle((x, y), 0.5)
ax.add_patch(circle)

def on_key(event):
    global x, y
    
    if event.key == 'w':
        y += 1
    elif event.key == 's':
        y -= 1
    elif event.key == 'a':
        x -= 1
    elif event.key == 'd':
        x += 1
    
    circle.center = (x, y)
    fig.canvas.draw()

# Connect keyboard event
fig.canvas.mpl_connect('key_press_event', on_key)

plt.title("Use W A S D keys to move the circle")
plt.grid()
plt.show()
