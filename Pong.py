# simple pong
import turtle

wn = turtle.Screen()  #make a windowed screen
wn.title("PONG")      #give the screen a title
wn.bgcolor("black")   #make bgcolor of screen to be black
wn.setup(width=800,height=600) #specifying the dimensions of the screen the canvas has 0 0 in center with +400 -400 and +300 -300 as max cordinates
wn.tracer(0) #stop updating the screen at any given time (speeds the game up significantally)

#score
score_a=0
score_b=0

# paddle A
paddle_a = turtle.Turtle() # creates a  turtle object
paddle_a.speed(0) # sets the speed of the animation to the maximum possible speed
paddle_a.shape("square") # sets shape
paddle_a.color("white") # sets color
paddle_a.shapesize(stretch_wid=5,stretch_len=1) #changes the square shape into a more rectangular shape 
paddle_a.penup() # makes it so a line isnt drawn when moving
paddle_a.goto(-350,0) # positions the shape at X -350 and Y 0

# paddle B 
paddle_b = turtle.Turtle() # creates a  turtle object
paddle_b.speed(0) # sets the speed of the animation to the maximum possible speed
paddle_b.shape("square") # sets shape
paddle_b.color("white") # sets color
paddle_b.shapesize(stretch_wid=5,stretch_len=1) #changes the square shape into a more rectangular shape 
paddle_b.penup() # makes it so a line isnt drawn when moving
paddle_b.goto(350,0) # positions the shape at X 350 and Y 0

# ball
ball = turtle.Turtle() #turtle object
ball.speed(0) #sets speed to max
ball.shape("square") # makes it a square shape
ball.color("white") # makes the color white
ball.penup() # line isnt drawn when moving
ball.goto(0,0) # sets the cordinates to X0 Y0
ball.dx = 0.15
ball.dy = 0.15

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center",font=("courier",24,"normal"))

# functions

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

# Main game loop

while True:
    wn.update() # every time the game runs it updates the screen

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))

    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("courier",24,"normal"))

    #ball paddle collision

    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 :
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 :
        ball.setx(-340)
        ball.dx *= -1