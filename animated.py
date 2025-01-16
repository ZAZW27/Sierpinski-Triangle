import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

points = [(-50, -30), (0, 70), (50, -30), (-50, -30)]
initDot = (0, 0)
x, y = zip(*points)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-50, 60)
ax.set_ylim(-30, 80)
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Coba")

gridGap = 10
ax.set_xticks(range(-50, 60, gridGap))
ax.set_yticks(range(-30, 80, gridGap))
ax.grid(False)

prevDot = [initDot[0], initDot[1]]
assignedData = [prevDot]

dots, = ax.plot([], [], 'o', markersize=2, color='black', alpha=0.5)

ax.plot(x, y, color='black', label='Sierpinski triangle')

x_data = []
y_data = []
countDot = 1
def update(frame):
    global prevDot, countDot
    pickCorner = random.randint(0, 2)
    xDot = float((prevDot[0] + x[pickCorner]) / 2)
    yDot = float((prevDot[1] + y[pickCorner]) / 2)

    # Update the x and y data
    x_data.append(xDot)
    y_data.append(yDot)

    # Update the plot with the new data
    dots.set_data(x_data, y_data)

    prevDot = [xDot, yDot]
    assignedData.append(prevDot)
    
    print(f"dot: {countDot}")
    countDot = countDot + 1

    return dots,  

ani = FuncAnimation(fig, update, frames=10000000, interval=1, blit=True)

plt.show()
