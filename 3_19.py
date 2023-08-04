import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

turtle.penup()
turtle.hideturtle()
turtle.speed(0)

turtle.goto(TARGET_LLEFT_X,TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0,0)
turtle.setheading(NORTH)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = float(input("Введите угол выстрела снаряда: "))
force = float(input("Введите пусковую силу от 1 до 10: "))


distance = force*FORCE_FACTOR

turtle.pendown()
turtle.setheading(angle)
turtle.forward(distance)

if  (turtle.xcor()>=TARGET_LLEFT_X and
    turtle.xcor()<=(TARGET_LLEFT_X+TARGET_WIDTH) and
    turtle.ycor()>=TARGET_LLEFT_Y and
    turtle.ycor()<=(TARGET_LLEFT_Y+TARGET_WIDTH)):
    print("Вы попали")


elif (turtle.xcor()<TARGET_LLEFT_X and
    turtle.ycor()>=0):
    print("Бейте правее")

elif (turtle.xcor()>(TARGET_LLEFT_X+TARGET_WIDTH) and
    turtle.ycor()>=0):
    print("Бейте левее")

elif (turtle.xcor()>=0 and
      turtle.ycor()<TARGET_LLEFT_Y):
    print("Бейте выше")

elif (turtle.xcor()>=0 and
      turtle.ycor()>(TARGET_LLEFT_Y+TARGET_WIDTH)):
    print("Бейте ниже")
    
else:
    print("Вы промахнулись")




    

    
    



    


