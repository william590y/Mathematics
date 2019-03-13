import random
print('Welcome to my Monte Carlo Simulation!')
while True:
 iterations = input('How many steps? ')
 steps = 0
 x = 0
 y = 0
 while int(steps) < int(iterations):
  z = random.randint(1,4)
  if z == 1:
   x = x+1
  elif z == 2:
   x = x-1
  elif z == 3:
   y = y+1
  elif z == 4:
   y = y-1
  steps = steps + 1
 if int(steps) >= int(iterations):
  print('object is at coordinates:' + str(x) + ', ' + str(y))
