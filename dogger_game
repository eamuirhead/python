"""
CSC 111: Final Project
Author: Elizabeth Muirhead
A program to make the Frogger Game

To run you need the following:
    - access to the python graphics module
    - a file name "beagle.gif" with approximate dimensions 140 x 85 - this file
        is the character that moves through the game
    - python version 3.0 or higher
"""

from graphics import *
import random



# GLOBALS

# width and height of window can be access in all functions
WIDTH = 1200
HEIGHT = 800



# CLASSES

'''This class creates the beagle object, draws in in the window, and moves it with each click.
It also checks if there's a collision or a successful road crossing'''
class Beagle:

    # constructor: initializes the number of lives and points
    def __init__(self, x, y):
        filename = "beagle.gif"  
        self.beagle = Image(Point(x,y), filename)
        self.points = 0
        self.lives = 3
        

    # draws beagle
    def create(self, win):
        self.beagle.draw(win)


    # moves beagle
    def beagle_move(self, click):
        
        # gets click 
        self.y = click.getY()

        # if click is above road, object moves up
        if self.y < HEIGHT*0.2:
            self.beagle.move(0, -80)

        # if click is below road, object moves down           
        if self.y > HEIGHT*0.6:
            self.beagle.move(0, 80)


    # checks if car and beagle are at the same point and moves it
    def collision(self,car_x, car_y, back):

        location = self.beagle.getAnchor()

        self.beagle_x = location.getX()
        self.beagle_y = location.getY()

        # checks if car is too close to dog
        if car_x in range(int(self.beagle_x-70), int(self.beagle_x+70)) and car_y in range(int(self.beagle_y-80), int(self.beagle_y+80)):
            # subtracts a life 
            self.lives -= 1

            # moves dog back to start
            self.beagle.move(0, back)

            
    # checks if beagle made it across the road
    def across(self, win):

        location = self.beagle.getAnchor()
        self.y = location.getY()

        # checks if dog makes it across
        if self.y < 75:
            # adds a point
            self.points += 1

            # moves beagle back to start
            self.beagle.move(0, HEIGHT-150)


    # returns the number of lives
    def get_lives(self):
        return self.lives


    # returns the number of points
    def get_points(self):
        return self.points



'''Banner class creates the banner and has a method to draw it. It can be drawn
and redraws to update the values.'''
class Banner:

    # constructor: initializes a banner of text    
    def __init__(self, x_posit, y_posit, message, win):
        self.text = Text(Point(x_posit, y_posit), message)
        self.text.setSize(20)
        self.win = win
        self.x_posit = x_posit
        self.y_posit = y_posit

    # draws the banner    
    def draw(self):
        self.text.draw(self.win)
        self.text.setSize(36)


    # undraws and redeaws the banner with the updated value
    def re_draw(self, message):
        self.text.undraw()
        self.text = Text(Point(self.x_posit, self.y_posit), message)
        self.draw()


    # sets the text color
    def set_color(self, color):
        self.text.setTextColor(color)


        
'''The Car class takes X and Y value to create a car objects, draw the
car objects on a window, and move the car objects. The speed are direction
are based on parameters that can be passed in. The class also has getter
funtions to get the position of a car object.'''
class Car:

    # constructor: initalize the parts of the car
    def __init__(self, x, y):
        
        p1 = Point(x-70,y-30)
        p2 = Point(x+70, y+30)

        # the components of the cars body
        body = Rectangle(p1, p2)
        top = Polygon(Point(x-50, y-30), Point(x+50, y-30), Point(x+50, y-60), Point(x-50, y-60))
        front_wheel = Circle(Point(x-35, y+30), 20)
        back_wheel = Circle(Point(x+35, y+30), 20)

        # the colors of the car
        front_wheel.setFill("black")
        back_wheel.setFill("black")
        rand_color = color_rgb(random.randint(0,150),random.randint(175,250), random.randint(125, 250))
        body.setFill(rand_color)
        top.setFill(rand_color)
        
        # list of all parts of the car
        self.part_lst = [back_wheel, top, body, front_wheel]


    # draws each part of the car in the window       
    def draw(self, window):

        for part in self.part_lst:
            part.draw(window)

            
    # makes the car move
    def move(self, dx, dy):

        # finds center of car
        center = self.part_lst[2].getCenter()
        x_center = center.getX()

        # moves car
        for part in self.part_lst:
            part.move(dx, dy)
            part.move(dx, -dy)

            # if the car gets too close to the end, it wraps to other side
            if x_center < 0 and dx < 0:
                part.move(WIDTH+100, 0)

            if x_center > 1290 and dx > 0:
                part.move((WIDTH*-1)-100, 0)

    # gets x corordinate of center of car
    def get_x(self):
        center = self.part_lst[2].getCenter()
        x = center.getX()
        return x


    # gets y corordinate of center of car
    def get_y(self):
        center = self.part_lst[2].getCenter()
        y = center.getY()
        return y



# HELPER FUNCTION

# draws the road
def draw_road(window):

    # sets the two boundries for the road
    road_line1 = int(HEIGHT * (.2))
    road_line2 = int(HEIGHT * (.6))

    # draws street in window and makes it gray
    street = Rectangle(Point(0, road_line1), Point(WIDTH, road_line2))
    street.setFill("slate gray")
    street.draw(window)

    # passes road_lines into function that draws the yellow dividers
    street_lines(road_line1, road_line2, window)

    
# draws yellow dividers 
def street_lines(road_line1, road_line2, window):

    center = int((road_line1 + road_line2)/2)

    # draws yellow lines based on length of the road
    for i in range(0, WIDTH, 30):
        rectangle_one = Polygon(Point(i, center-3), Point(i+20, center-3), Point(i+20, center-10), Point(i, center-10))
        rectangle_one.setFill("yellow")
        rectangle_one.draw(window)

        rectangle_two = Polygon(Point(i, center+3), Point(i+20, center+3), Point(i+20, center+10), Point(i, center+10))
        rectangle_two.setFill("yellow")
        rectangle_two.draw(window)



# MAIN

def main():

    # holds the car objects
    upper_car_lst = []
    lower_car_lst = []

    # initial lives and points values
    current_lives = 3
    current_points = 0

    # draws window
    win = GraphWin('Dogger', WIDTH, HEIGHT, autoflush=False)
    draw_road(win)

    # calls the banner class to create two banner
    banner = Banner(89, 35, "Points: 0", win)
    banner2 = Banner(170, 80, "Lives Remaining: 3", win)

    # creates the beagle object using the beagle class
    beagle = Beagle(600, 560)

    # draws banner and beagle
    beagle.create(win)
    banner.draw()
    banner2.draw()

    # uses the Car class
    # creates the car objects for the upper car list
    for i in range(70, WIDTH, 300):
        y_position = int(HEIGHT * .3)
        car = Car(i, y_position)
        car.draw(win)
        upper_car_lst.append(car)

    # uses the Car class
    # creates the car objects for the lower car list
    for i in range(70, WIDTH, 300):
        y_position2 = int(HEIGHT * .5)
        car2 = Car(i, y_position2)
        car2.draw(win)
        lower_car_lst.append(car2)
        
    # loop runs while the user still has lives
    while current_lives > 0:
        
        # moves the cars in the list
        for elem in upper_car_lst:
            elem.move(-1.75, 0)
            # checks for collisions and checks if beagle made it across
            beagle.collision(elem.get_x(), elem.get_y(), HEIGHT*0.6)
            # print (col_check)
            beagle.across(win)                           
                
        for elem in lower_car_lst:
            elem.move(2.5, 0)
            beagle.collision(elem.get_x(), elem.get_y(), HEIGHT*0.4)
            beagle.across(win)

        # if you lose a point, the lives banner gets updated
        if beagle.get_lives() < current_lives:
            banner2.re_draw("Lives Remaining: "+str(beagle.get_lives()))
            current_lives = beagle.get_lives()

        # if user gets a point, the points banner gets updated
        if beagle.get_points() > current_points:
            banner.re_draw("Points: "+str(beagle.get_points()))
            current_points = beagle.get_points() 
            
        update()

        # checks for user click
        click = win.checkMouse()
        # if user clicks, the beagle moves
        if click != None:
            beagle.beagle_move(click)

    # prints GAME OVER
    game_over = Banner(WIDTH/2, HEIGHT/1.5, "GAME OVER", win)
    game_over.draw()
    game_over.set_color("red")
    

main()

