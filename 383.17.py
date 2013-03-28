# Problem 17

# Creates a GraphicsGroup class (in this case a face) made up of separate pieces. The face moves to where the user clicks.



from graphics import *

class GraphicsGroup:

    def __init__(self, anchor):
        self.anchor=anchor
        objects=[]
        self.objects=objects

    def getAnchor(self):
        return self.anchor

    def addObject(self, gObject):
        self.objects.append(gObject)

    def move(self, dx,dy):
        for object in self.objects:
            object.move(dx,dy)
        self.anchor.move(dx,dy)

    def draw(self,win):
        for object in self.objects:
            object.draw(win)

    def undraw(self):
        for object in self.objects:
            object.undraw()


def main():

    #Create window
    win = GraphWin()

    # Create face object
    face=GraphicsGroup(Point(100,100))
    circle = Circle(Point(100,100),30)
    face.addObject(circle)
    rightEye = Circle(Point(110,90),5)
    face.addObject(rightEye)
    leftEye = Circle(Point(90,90),5)
    face.addObject(leftEye)
    mouth = Line(Point(90,120), Point(110,120))
    face.addObject(mouth)

    # Draw face
    face.draw(win)

    # User clicks to move face
    for i in range(5):
        print ("Please click anywhere in the window to move the face.")
        click=win.getMouse()
        x = click.getX()
        y = click.getY()
        anchor=face.getAnchor()
        x2=anchor.getX()
        y2=anchor.getY()
        dx = x-x2
        dy = y-y2
        face.undraw()
        face.move(dx,dy)
        face.draw(win)


# Close window
    print ()
    print ("Click to close the window.")
    win.getMouse()
    win.close()

if __name__=='__main__':
    main ()











