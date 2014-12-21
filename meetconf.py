import turtle

turtle.pd()
turtle.shape("turtle")

def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x+60,y)
	turtle.goto(x+60,y+60)
	turtle.goto(x,y+60)
	turtle.goto(x,y)
draw_square(0,0)


def draw_triangle(x,y):
	turtle.pu()
	turtle.goto(x,y)
	turtle.pd()
	turtle.goto(x+60,y+85)
	turtle.goto(x+85,y)
	turtle.goto(x,y)
draw_triangle(50,50)

turtle.onscreenclick(draw_square, btn=1, add=True)
turtle.onscreenclick(draw_triangle, btn=3, add=True)

def myfun():turtle.color("green")
turtle.getscreen().onkeypress(myfun,"Up")
turtle.getscreen().listen()

def myfun():turtle.color("yellow")
turtle.getscreen().onkeypress(myfun,"Down")
turtle.getscreen().listen()

def myfun():turtle.color("blue")
turtle.getscreen().onkeypress(myfun,"Right")
turtle.getscreen().listen()

def myfun():turtle.color("purple")
turtle.getscreen().onkeypress(myfun,"Left")
turtle.getscreen().listen()


turtle.mainloop()
