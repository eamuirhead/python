"""
CSC 111, Lab 9
Author: Sara Mathieson (modified from Lab 8 solution)
Author: Elizabeth Muirhead and Maddy Kulke
A program to draw a fractal tree using recursion.
"""


from graphics import *
import math
import random


# GLOBALS

theta = 0.7 # angle of each branch away from its trunk
petal_color = "magenta4" # color of the petals
center_color = "yellow" # color of the center of the flower
sky_color = "light pink" # color of the sky/background
ground_color = "dark green" # color of the ground
branch_color = "navy" # color of the branches
flower_lst = [] #global 


# CLASSES

# Creases flower object
class Flower:

    #initializes instance variable
    def __init__(self, x, y): 
        # make a yellow center for the flower
        center = Circle(Point(x,y),2)
        center.setFill(center_color)
        center.setOutline(center_color)

        # set petal length and pick a random orientation for the flower
        petal_len = 18
        angle = random.uniform(0,2*math.pi)
        
        # make four petals using helper function
        petal1 = self.make_petal(x, y, petal_len,angle)
        petal2 = self.make_petal(x, y, petal_len,angle+math.pi/2)
        petal3 = self.make_petal(x, y, petal_len,angle+math.pi)
        petal4 = self.make_petal(x, y, petal_len,angle+3*math.pi/2)

        # list with all the components iof the flower
        self.part_lst = [center, petal1, petal2, petal3, petal4]

    # builds and returns a petal
    def make_petal(self, x, y, length, angle):
        
        # first point closest to the center
        p1 = Point(x,y)

        # left-most point
        dx2 = length/2*math.cos(angle-0.3)
        dy2 = length/2*math.sin(angle-0.3)
        p2 = Point(x+dx2,y+dy2)

        # furthest point from the center
        dx3 = length*math.cos(angle)
        dy3 = length*math.sin(angle)
        p3 = Point(x+dx3,y+dy3)

        # right-most point
        dx4 = length/2*math.cos(angle+0.3)
        dy4 = length/2*math.sin(angle+0.3)
        p4 = Point(x+dx4,y+dy4)

        # create the diamond-shaped petal
        petal = Polygon(p1,p2,p3,p4)
        petal.setFill(petal_color)
        petal.setOutline(petal_color)
        return petal


    # draws all parts in part list of flower
    def draw(self, window): 
        for part in self.part_lst: 
            part.draw(window)   
        
        
    # moves all parts in part list    
    def move(self, dx, dy): 
        for part in self.part_lst:            
            part.move(dx, dy)


    # gets center of circle in part list, returns true if flower center is less than height
    def is_above_ground(self, y): 
        flower_center = self.part_lst[0].getCenter()
        y_height = flower_center.getY()
        if y_height < y:
            return True
        else:
            return False


# HELPER FUNCTIONS

# recursively draws a fractal tree
def draw_tree(window, order, x, y, length, angle):

    # compute the coordinates of end of the current branch
    dx = length * math.cos(angle)
    dy = length * math.sin(angle)
    x2 = x + dx
    y2 = y + dy

    # draw current branch
    branch = Line(Point(x,y), Point(x2,y2))
    branch.setFill(branch_color)
    branch.setWidth(order) # make the higher order branches thicker
    branch.draw(window)

    # base case: at the leaves, draw a flower
    if order == 0:
        flower = Flower(x2,y2)
        flower.draw(window)
        flower_lst.append(flower)
        

    # recursion case: if order > 0, draw two subtrees
    else:
        new_len = length*0.7
        draw_tree(window, order-1, x2, y2, new_len, angle-theta) # "left" branch
        draw_tree(window, order-1, x2, y2, new_len, angle+theta) # "right" branch


# MAIN

def main():

    # set up the graphics window
    width = 800
    height = 600
    win = GraphWin("Fractal Tree", width, height)
    win.setBackground(sky_color)

    # draws the ground
    ground = Rectangle(Point(0,height-80), Point(width,height))
    ground.setFill(ground_color)
    ground.setOutline(ground_color)
    ground.draw(win)

    # set up parameters for our call to the recursive function
    order = 6
    x_start = width/2   # middle of the window
    y_start = height-10 # close to the bottom of the window
    angle = -math.pi/2  # initial branch (trunk) pointing *upwards*
    length = 200        # length of initial branch (trunk)

    # calls recursive function to draw tree
    draw_tree(win, order, x_start, y_start, length, angle)

    # loops through the flowers
    for f in flower_lst:
        # while loop checks to see if flower_Center y is less than height-20
        while f.is_above_ground(height-(random.randint(20,70))):
            # while true, flower continues to move down by 10
            f.move(0, 10) 
    

    # close on click
    win.getMouse()
    win.close()


main()
