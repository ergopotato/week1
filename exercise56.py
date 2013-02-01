#Exercise 5.6
# x = raw_input('Set ??? length?\n')
# length =raw_input('Set side length?\n')

#Note:
#t = the turtle.
#length = the length of the segment the turtle draws.
#angle = angle of turn the turtle turns when lt or rt is called.

# def draw(t, length, n):
#   if n==0:
# k    return

#   angle = 35
#   fd(t, length*n)
#   lt(t, angle)
#   draw(t, length, n-1)
#   rt(t, 3*angle)
#   draw(t, length, n-1)
#   lt(t, angle)
#   bk(t, length*n)

world = TurtleWorld()
t = Turtle()

def koch(t, x):
    if x < 3:
      fd(t, x)
    koch (t, x/3)
    lt(t,60)
    koch (t, x/3)
    rt(t,120)
    koch (t, x/3)
    lt(t,60)
    koch (t, x/3)
