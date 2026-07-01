# import required modules
import turtle
import time 
import random 

delay = 0.1
score = 0
high_score = 0

# creating a window screen 
wn = turtle.Screen()
wn.title("Snake Game | Created by Menna Ayman") 
wn.bgcolor("#131940")
wn.setup(width=600, height=600) 
wn.cv._rootwindow.resizable(False, False)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("#FF6BDC")
head.penup()     # stop drawing lines when moving
head.speed(0)
head.goto(0, 0)
head.direction = "stop"


# food in the game

food = turtle.Turtle()
food.penup()        

colors = random.choice(["#FF1493", "#40E0D0", "#FFD700"])
shapes = random.choice(["triangle", "square"])
food.shape(shapes)
food.color(colors)
food.speed(0)
food.goto(0, 100)

# Score displays
pen = turtle.Turtle()
pen.shape("square")
pen.color("#FF6BDC")          
pen.speed(0)
pen.penup()
pen.goto(0, 250)            
pen.hideturtle()
pen.write("Score: 0  High Score: 0", align="center", font=("Terminal", 18, "bold"))
signature = turtle.Turtle()
signature.hideturtle()
signature.penup()
signature.color("#FF6BDC")
signature.goto(0, -285)
signature.write(
    "Created by Menna Ayman",
    align="center",
    font=("Terminal", 12, "bold")
)

# assing key direction
def goup():
    if head.direction !="down":
        head.direction="up" 

def godown():
    if head.direction !="up":
        head.direction="down"   

def goleft():
    if head.direction !="right":
        head.direction="left" 

def goright():
    if head.direction !="left":
        head.direction="right"        

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# key binding 
wn.listen()   
wn.onkeypress(goup, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft,"Left")
wn.onkeypress(goright, "Right")

segements = []
wn.tracer(0) 

# Main Gameplay
while True:
    wn.update()

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        colors = random.choice(["#FF1493", "#40E0D0", "#FFD700"])
        shapes = random.choice(["triangle", "square"])
        food.shape(shapes)
        food.color(colors)

        for segment in segements:
            segment.penup()
            segment.hideturtle()
            segment.goto(1000, 1000)
        segements.clear()

        score = 0
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Terminal", 18, "bold"))

    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#FF9CEE")
        new_segment.penup()
        segements.append(new_segment)
        

        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Terminal", 18, "bold"))

    for index in range(len(segements) - 1, 0, -1):
        x = segements[index - 1].xcor()
        y = segements[index - 1].ycor()
        segements[index].goto(x, y)

    if len(segements) > 0:
        x = head.xcor()
        y = head.ycor()
        segements[0].goto(x, y)

    move()
         
    time.sleep(delay)