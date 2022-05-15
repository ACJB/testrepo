import turtle
t = turtle.Pen()

for x in range(360):
    t.forward(x)
    t.left(59)

# hashtag use for remark purpose same as C++ 

##lesson 1
import turtle # open/import turtle graphics 
turtle.showturtle() #shoeing the pointer
turtle.write("Well Hello") #the programme will show anything written in this line
turtle.forward(300) # the pointer will move forward 300 pixel
turtle.color("red") # this code can change the pointer color
turtle.left(90) #enable to rotate the pointer direction
turtle.forward(300)
turtle.goto(0,50) # the Pointer will procced to the given Coordinate.
turtle.goto(0,0) # the Pointer will procced to origin Coordinate.
turtle.penup()# the Pointer will "lift up the pen", so when it move to another coordiante no line will be drawn.
turtle.goto(0,300) # the Pointer will procced to the given Coordinate (X,Y). in this line the result will show the pointer moves to the coordinate but no line is drawn.
turtle.pendown() #the Pointer will "put down the pen" and code after this line the pointer moves to a new coordinate a line will be drawn.
turtle.circle(100) #the code "turtle.circle" initiate to draw a circle where "(100)" is the radius

