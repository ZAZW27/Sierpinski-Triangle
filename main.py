import matplotlib.pyplot as plt
import random

points = [(-50, -30), (0, 70), (50, -30), (-50, -30)]
initDot = (-17, -21)
x, y = zip(*points)

def createTriangle(): 
    plt.plot(x, y, color='black', label='Sierpinski triangle')
    
    calculateDots()
    
def calculateDots(): 
    plt.plot(initDot[0], initDot[1], marker='o', markersize=2 , color='black')
    
    prevDot = [initDot[0], initDot[1]]
    assignedData = [prevDot]
    for _ in range(0, 5000):
        pickCorner = random.randint(0, 2)
        xDot = float((prevDot[0] + x[pickCorner]) / 2)
        yDot = float((prevDot[1] + y[pickCorner]) / 2)
        
        plt.plot(xDot, yDot, marker='o', markersize=2 , color='black', alpha=0.5)
        
        prevDot = [xDot, yDot]
        assignedData.append(prevDot)
    with open('assignedDot.txt', 'w') as file:
        file.write(',\n'.join(map(str, assignedData)))

def main(): 
    gridGap = 1
    createTriangle()
    
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Coba")

    # plt.legend()

    plt.xticks(range(-50, 60, gridGap))
    plt.yticks(range(-30, 80, gridGap))

    plt.grid(False)
    plt.show()
    
main()