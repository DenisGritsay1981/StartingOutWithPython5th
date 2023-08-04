import turtle

def main():
    
    turtle.speed(9)
    drawBase(100)
    drawMidSection(50)
    drawArms()


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
    
    
    
                       


    



drawHead()
drawHat()
    


    

    


          
        
    





        












              







    
    

 







    

    

