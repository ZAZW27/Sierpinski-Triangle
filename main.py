import matplotlib.pyplot as plt

points = [(-50, -30), (0, 70), (50, -30), (-50, -30)]

x, y = zip(*points)

plt.plot(x, y, color='black', label='Sierpinski triangle')

for i in range(0, 10): 
    plt.plot(i+10, i+10, marker='o', markersize=2 , color='black')

plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Coba")

plt.legend()

plt.xticks(range(-50, 60, 1))
plt.yticks(range(-30, 80, 1))

plt.grid(False)
plt.show()