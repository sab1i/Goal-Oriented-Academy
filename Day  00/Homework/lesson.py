from turtle import *
width(5)


#body
color('blue')
begin_fill()
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()


penup()
goto(200,200)
pendown()


#roof
color('green')
begin_fill()
left(180)
left(45)
forward(141)
left(90)
forward(141)
end_fill()



penup()
goto(80,0)
pendown()


#door
color("black")
begin_fill()
right(45)
right(90)
forward(80)
right(90)
forward(40)
right(90)
forward(80)
end_fill()

penup()
goto(20,180)
pendown()
#window1
color("black")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
goto(180,180)
pendown()


#window2
color("black")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()





exitonclick()