# This is a "try-out" of Pong 
#Date : 3 August 
#Python experience : 0% 


#Turtle is a is a pre-installed Python library, thats helps with the graphic of game developments. 
#that enables users to create pictures and shapes by providing them with a virtual canvas.
import turtle 


#win stands for window
win = turtle.Screen()
win.title("Pong by Silinda")
win.bgcolor("white")
win.setup(width=800, height=600)
win.tracer(0)  #stops the window from updating

#score 
Score_1 = 0 
Score_2 = 0 

#The paddles and ball 
# Paddle 1
paddle_1 = turtle.Turtle() # turtle object, where the "turtle" is the module name, and "Turtle" is the class name
paddle_1.speed(0) # this is the ANIMATION speed and not the paddle speed 
paddle_1.shape("square") 
paddle_1.color("black")
paddle_1.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_1.penup() #makes sure that the moving object added to the game does not draw anything on the window/screen 
paddle_1.goto(-350, 0) 

# Paddle 2 
paddle_2 = turtle.Turtle() 
paddle_2.speed(0)
paddle_2.shape("square") 
paddle_2.color("black")
paddle_2.shapesize(stretch_wid= 5, stretch_len= 1)
paddle_2.penup() 
paddle_2.goto(350, 0) 

# Ball 
Ball = turtle.Turtle() 
Ball.speed(0) 
Ball.shape("circle") 
Ball.color("black")
Ball.penup() 
Ball.goto(0, 0) 
Ball.dx = 2 
Ball.dy = -2 


# Pen, just like the turtle module 
# Score on the screen 
pen = turtle.Turtle() 
pen.speed(0)
pen.color("black") 
pen.penup()
pen.hideturtle()
pen.goto(0, 260) 
pen.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


#Functions 
#Movements of the paddles 
def paddle_1_up(): #Defining the functions, this function is the up function 
    y = paddle_1.ycor() #ycor is from the module, and its function is to return the y coordinate. 
    y += 20 # adds 20 pixels to the y coordinate
    paddle_1.sety(y) #adds y to the new y 

def paddle_1_down(): 
    y = paddle_1.ycor() 
    y -= 20 
    paddle_1.sety(y) 


def paddle_2_up(): 
    y = paddle_2.ycor() 
    y += 20 
    paddle_2.sety(y) 

def paddle_2_down(): 
    y = paddle_2.ycor() 
    y -= 20 
    paddle_2.sety(y) 

#Keyboard binding 
win.listen() # listening to keyboard inputs 
win.onkeypress(paddle_1_up, "w") #when the user presses w, the function paddle_1_up gets called. 
win.onkeypress(paddle_1_down, "s")
win.onkeypress(paddle_2_up, "Up")
win.onkeypress(paddle_2_down, "Down")

#Main game loop
#the .. game code 
while True:
    win.update() #everytime the loop runs, it updates the screen. 
    
    #Ball movement 
    Ball.setx(Ball.xcor() + Ball.dx) 
    Ball.sety(Ball.ycor() + Ball.dy)

    #Top and bottom Borders 
    if Ball.ycor() > 290: 
        Ball.sety(290)
        Ball.dy *= -1  # reverses the direction of the ball

    if Ball.ycor() < -290: 
        Ball.sety(-290)
        Ball.dy *= -1
    
    #Left and right Borders 
    if Ball.xcor() > 390: 
        Ball.goto(0, 0) 
        Ball.dx *= -1
        Score_1 += 1 
        pen.clear() # clearin whats on the screen
        pen.write("Player 1: {} Player 2: {}".format(Score_1, Score_2), align="center", font=("Courier", 24, "normal"))

    
    if Ball.xcor() < -390: 
        Ball.goto(0, 0) 
        Ball.dx *= -1
        Score_2 += 1 
        pen.clear() # clearin whats on the screen
        pen.write("Player 1: {} Player 2: {}".format(Score_1, Score_2), align="center", font=("Courier", 24, "normal"))

    
    #Paddle and ball coliding 
    #
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddle_2.ycor() + 40 and Ball.ycor() > paddle_2.ycor() -40): 
        Ball.setx(340)
        Ball.dx *= -1
    
    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddle_1.ycor() + 40 and Ball.ycor() > paddle_1.ycor() -40): 
        Ball.setx(-340)
        Ball.dx *= -1
