# Author: Elizabeth Muirhead
# A Dice Rolling Class

from graphics import *
import random

# creates the button object at the bottom of the screen
class Button:

    def __init__(self, x, y, w, h, label):

        # set up the boundaries of the button
        self.xmin, self.xmax = x - w/2, x + w/2
        self.ymin, self.ymax = y - h/2, y + h/2

        # ranges of x and y for testing
        self.x_range = range(int(self.xmin), int(self.xmax))
        self.y_range = range(int(self.ymin), int(self.ymax))

        # rectangle for the outline
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setWidth(3)

        # text of the button
        self.text = Text(Point(x,y), label)

    # draws the botton in the window
    def draw(self, window):
        self.rect.draw(window)
        self.text.draw(window)

     # checks if the button was clicked       
    def clicked(self, point):
        if point.getX() in self.x_range and point.getY() in self.y_range:
            return True
        else:
            return False

# creates the dice object
class DieView:

    def __init__(self, x, y, size):

        # background of dice and color of the pips
        self.background = "plum"
        self.foreground = "darkred"

        # dimentions for the dice
        p1 = Point(x-size/2,y-size/2)
        p2 = Point(x+size/2,y+size/2)
        self.square = Rectangle(p1, p2)
        self.square.setFill(self.background)

        self.pip_size = 5
        
        # draw all pips
        offset = size/4
        pip0 = self.make_pip(x-offset, y-offset)
        pip1 = self.make_pip(x-offset, y)
        pip2 = self.make_pip(x-offset, y+offset)
        pip3 = self.make_pip(x, y)
        pip4 = self.make_pip(x+offset, y-offset)
        pip5 = self.make_pip(x+offset, y)
        pip6 = self.make_pip(x+offset, y+offset)

        self.pip_lst = [pip0, pip1, pip2, pip3, pip4, pip5, pip6]

    # draws the dice and the pips
    def draw(self, window):
        self.square.draw(window)
        for pip in self.pip_lst:
            pip.draw(window)

    # creates each pip
    def make_pip(self, x, y):
        pip = Circle(Point(x,y), self.pip_size)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        return pip

    # pills in the correct pips for each dice value
    def set_value(self, value):

        # resets each pip to the color of the dice so it's not visable
        for pip in self.pip_lst:
            pip.setFill(self.background)

        # pips that need to be colored for each roll
        if value == 1:
            pips_on = [3]
        elif value == 2:
            pips_on = [0,6]
        elif value == 3:
            pips_on = [0,3,6]
        elif value == 4:
            pips_on = [0,2,4,6]
        elif value == 5:
            pips_on = [0,2,3,4,6]
        elif value == 6:
            pips_on = [0,1,2,4,5,6]

        # colors the correct pips
        for i in pips_on:
            pip = self.pip_lst[i]
            pip.setFill(self.foreground)


def main():

    # creates the win everything will sit in
    win = GraphWin("Dice Roller")

    # parameters: (x,y) of center, width, height, label
    roll = Button(100, 150, 60, 20, "Roll Dice")
    roll.draw(win)

    # parameters: (x,y) of center, size
    die1 = DieView(50,70,60)
    die2 = DieView(150,70,60)
    die1.draw(win)
    die2.draw(win)

    # when the roll button is clicked, it roles the dice
    while True:
        p = win.getMouse()
        if roll.clicked(p):
            die1.set_value(random.randint(1,6))
            die2.set_value(random.randint(1,6))
        else:
            print("not clicked")
main()
