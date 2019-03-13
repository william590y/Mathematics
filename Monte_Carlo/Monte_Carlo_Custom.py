import random
print('Welcome to my Monte Carlo Simulation!')
while True:
 iterations = input('How many steps? ')
 right = float(input('Probability of moving right? (percentage) '))
 left = float(input('Probability of moving left? (percentage) '))
 up = float(input('Probability of moving up? (percentage) '))
 down = float(input('Probability of moving down? (percentage) '))
 steps = 0
 x = 0
 y = 0
 while int(steps) < int(iterations):
  z = random.uniform(0,10)
  if z < right/10:
   x = x+1
  elif z < left/10 + right/10:
   x = x-1
  elif z < left/10 + right/10 + up/10:
   y = y+1
  elif z < left/10 + right/10 + up/10 + down/10:
   y = y-1
  steps = steps + 1
 if int(steps) >= int(iterations):
  print('object is at coordinates:' + str(x) + ', ' + str(y))
