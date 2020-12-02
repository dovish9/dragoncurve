import turtle
import math as m
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0) # fastest speen, same as 20
t.shape("turtle")

# move initial position
t.penup()
t.goto(0,200)
t.pendown()

# changeable value: n: the curve moves 2^(n-1) times, length: length of a side
length = 5 # default = 5
n = 20 # an integer greater than or equal to 2

# return the number plus one, 4 is considered 0
def inc(x):
    if x==0 or x==1 or x==2:
        return x+1
    elif x==3:
        return 0

# color list
color=["rosybrown",
        "mediumpurple",
        "fuchsia",
        "cornflowerblue",
        "lime",
        "salmon",
        "crimson",
        "blue"]

# make a sequence for dragon curve, each number means deirection just like →: 0, ↑: 1, ←: 2, ↓: 3
sequence = list()
sequence.append(0) # first term of the sequence
for i in range(2, n+1, 1):
    for j in range(0, 2**(i-2), 1):
        x = inc(sequence[2**(i-2)-1-j])
        sequence.append(x)

# draw
for k in range(0,2**(n-1),1):
    t.setheading(90*sequence[k]) # 0: 0, 1: 90, 2: 180, 3: 270
    t.forward(length)
    if k==0:
        t.pencolor("white")
    else:
        t.pencolor(color[m.floor(m.log(k)+1)%8])
