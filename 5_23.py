import turtle

def main():
    
    turtle.speed(0)
    drawBase(100)
    drawMidSection(50)
    drawArms()
    drawHead(30)
    drawHat("red")

def drawBase(x):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.circle(x)

def drawMidSection(x):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    turtle.circle(x)

def drawArms():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(50,50)
    turtle.pendown()
    turtle.left(25)
    turtle.forward(50)
    turtle.left(25)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(275)
    turtle.forward(25)

    turtle.penup()
    turtle.goto(-50,50)
    turtle.pendown()
    turtle.left(215)
    turtle.forward(25)
    turtle.right(45)
    turtle.forward(50)
    turtle.left(25)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(275)
    turtle.forward(25)

def drawHead(x):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(25,113)
    turtle.pendown()
    turtle.circle(x)

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(15,130)
    turtle.pendown()
    turtle.circle(5)

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-5,130)
    turtle.pendown()
    turtle.circle(5)

    turtle.hideturtle()
    turtle.penup()
    turtle.goto(12,110)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(20)

def drawHat(x):
    turtle.hideturtle()
    

    turtle.penup()
    turtle.goto(15,145)
    turtle.fillcolor(x)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(180)
    turtle.forward(30)
    turtle.setheading(270)
    turtle.forward(30)
    turtle.setheading(360)
    turtle.forward(30)
    turtle.end_fill()

    
    turtle.penup()
    turtle.goto(25,145)
    turtle.fillcolor(x)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(20)
    turtle.setheading(180)
    turtle.forward(50)
    turtle.setheading(270)
    turtle.forward(20)
    turtle.setheading(360)
    turtle.forward(50)
    turtle.end_fill()
                       


    





    


    

    


          
        
    





        












              







    
    

 







    

    

