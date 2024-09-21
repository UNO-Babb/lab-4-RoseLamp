#TurtleGraphics.py
#Name:Rose
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(tim, sides):
    for s in range (sides):
        tim.forward(75)
        tim.right(360/sides)

#corner = (int)(input("what corner would you like filled? 1, 2, 3, 4")) 
    #if uncommented makes the fill corner function based on user input
def fillCorner(allie, corner):
    drawSquare(allie, 100)  
    if corner == 1:
        allie.begin_fill()
        drawSquare(allie, 50)
        allie.end_fill()
    if corner ==2:
        allie.forward(50)
        allie.begin_fill()
        drawSquare(allie, 50)
        allie.end_fill()
    if corner ==3:
        allie.forward(100)
        allie.right(90)
        allie.forward(50)
        allie.begin_fill()
        drawSquare(allie, 50)
        allie.end_fill()
    if corner ==4:
        allie.forward(100)
        allie.right(90)
        allie.forward(100)
        allie.right(90)
        allie.forward(50)
        allie.begin_fill()
        drawSquare(allie, 50)
        allie.end_fill()
def main():
    myTurtle = turtle.Turtle()
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    
    fillCorner(myTurtle, corner)#should work now based on user input and only fillcorner function that needs uncommented.
    
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    #fillCorner(myTurtle, 4)
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
