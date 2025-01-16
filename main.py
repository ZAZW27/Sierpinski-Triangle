import matplotlib.pyplot as plt
import random

points = [(-50, -30), (0, 70), (50, -30), (-50, -30)]
initDot = (30, -19)
x, y = zip(*points)

def createTriangle(): 
    plt.plot(x, y, color='black', label='Sierpinski triangle')
    
    calculateDots()
    
def calculateDots(): 
    plt.plot(initDot[0], initDot[1], marker='o', markersize=2 , color='black')
    
    for _ in range(0, 100):
        pickCorner = random.randint(0, 2)
        prevDot = [initDot[0], initDot[1]]
        xDot = float((prevDot[0] + x[pickCorner]) / 2)
        yDot = float((prevDot[1] + y[pickCorner]) / 2)
        
        plt.plot(xDot, yDot, marker='o', markersize=2 , color='black')
    

def main(): 
    createTriangle()
    
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Coba")

    plt.legend()

    plt.xticks(range(-50, 60, 1))
    plt.yticks(range(-30, 80, 1))

    plt.grid(False)
    plt.show()
    
main()