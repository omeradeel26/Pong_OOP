##################################################
# imports 

import random

###################################################
# classes 
class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH/2 #default in middle of screen
        self.y = SCREEN_LENGTH/2        
        self.dx = 3
        self.dy = 3
        
    def move(self):
        self.x += self.dx 
        self.y += self.dy
        
        if self.y <= 0:
            self.dy *=-1 
        elif self.y >= SCREEN_LENGTH:
            self.dy*=-1

    def draw(self):
        circle(self.x, self.y, 20)   
        
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.dy = 0
        
    def move(self):
        self.y+= self.dy
        if self.y > SCREEN_LENGTH-100:
            self.y = SCREEN_LENGTH-100
        if self.y < 0:
            self.y = 0
            
    def move_up(self): 
        self.dy = -3
            
    def move_down(self):
        self.dy = 3
        
    def stop_moving(self):
        self.dy = 0

    def draw(self): 
        fill(255)
        rect(self.x, self.y, 15, 100)
                
def collision_detection():
    if (ball.y >= player_1.y) and (ball.y <= player_1.y+100) and (player_1.x+10 >= ball.x): 
        ball.dx *=-1
    if (ball.y >= player_2.y) and (ball.y <= player_2.y+100) and (player_2.x <= ball.x):
        ball.dx*=-1

        
#################################################
# global/ object creation

SCREEN_WIDTH = 800
SCREEN_LENGTH = 600
ball = Ball()
player_1 = Paddle(25, SCREEN_LENGTH/2 - 50) 
player_2 = Paddle(SCREEN_WIDTH-40, SCREEN_LENGTH/2 - 50) 


################################################
# Processing Stuff

def setup(): #setup screen size, color etc.
    size(SCREEN_WIDTH, SCREEN_LENGTH)

def draw(): 
    background(0)
    collision_detection()
   
    ball.move()
    player_1.move()
    player_2.move()
    
    ball.draw()
    player_1.draw()    
    player_2.draw()
    

def keyPressed():
    if key == 'w' or key == "W":
        player_1.move_up()
    if key == 's' or key == "S":
        player_1.move_down()
        
    if keyCode == UP:
        player_2.move_up()
    if keyCode == DOWN:
        player_2.move_down()

def keyReleased():
    if key == "w":
        player_1.stop_moving()
    if key == "s":
        player_1.stop_moving()
        
    if keyCode == UP:
        player_2.stop_moving()
    if keyCode == DOWN:
        player_2.stop_moving()
