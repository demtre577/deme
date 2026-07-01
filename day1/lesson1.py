from turtle import*


#we wat to paint a house

#step 1: draw a squaner

speed(30)

width(7)
color("purple")

forward(200)
left(90)


forward(200)
left(90)


forward(200)
left(90)




forward(200)
left(90)

#end of square


#drawin a door


forward(70)
left(90)
forward(120) #heiling of the door
right(90)  
forward(60)
right(90)
forward(120)

penup()
goto(200, 200)
pendown()
      
begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()