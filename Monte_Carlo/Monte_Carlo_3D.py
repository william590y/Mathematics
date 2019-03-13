import random
print('Welcome to my 3D Monte Carlo Simulation!')
while True:
 iterations = input('How many steps? ')
 steps = 0
 x = 0
 y = 0
 z = 0
 while int(steps) < int(iterations):
  a = random.randint(1,6)
  if a == 1:
   x = x+1
  elif a == 2:
   x = x-1
  elif a == 3:
   y = y+1
  elif a == 4:
   y = y-1
  elif a == 5:
   z = z+1
  elif a == 6:
   z = z-1
  steps = steps + 1
 if int(steps) >= int(iterations):
  print('object is at coordinates:' + str(x) + ', ' + str(y) + ', ' + str(z))
