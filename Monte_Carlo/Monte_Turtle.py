import random
import turtle
fred = turtle.Pen()
print('Welcome to my Monte Carlo Simulation!')
while True:
 iterations = input('How many steps? ')
 n = int(input('How large of a step? '))
 fred.reset()
 steps = 0
 x = 0
 y = 0
 while int(steps) < int(iterations):
  z = random.randint(1,4)
  a = fred.xcor()
  b = fred.ycor()
  if z == 1:
   x = x+1
   fred.goto(a+n,b)
  elif z == 2:
   x = x-1
   fred.goto(a-n,b)
  elif z == 3:
   y = y+1
   fred.goto(a,b+n)
  elif z == 4:
   y = y-1
   fred.goto(a,b-n)
  steps = steps + 1
 if int(steps) >= int(iterations):
  print('object is at coordinates:' + str(int(x)) + ', ' + str(int(y)))
