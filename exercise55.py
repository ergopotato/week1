#Exercise 5.5
#Pictue of fractal drawn is


def draw(t, length, n):
  if n==0:
    return

  angle = 35
  fd(t, length*n)
  lt(t, angle)
  draw(t, length, n-1)
  rt(t, 3*angle)
  draw(t, length, n-1)
  lt(t, angle)
  bk(t, length*n)

world = TurtleWorld()
t = Turtle()
