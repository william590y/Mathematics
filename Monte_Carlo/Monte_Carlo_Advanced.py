#setup
import random
print('Welcome to my Monte Carlo simulation!')
while True:
 steps = int(input('How many steps? '))
 dimensions = input('How many dimensions? ')
 list_1 =  []
 list_2 =  []
 list_3 =  []
 list_4 =  []
 list_5 =  []
 step = 0
#variables
 for counter in range(int(dimensions)):
  list_1.append('var_' + str(int(counter) + 1) + ' = 0')
  exec(list_1[counter])
#operations
 for counter_2 in range(1,2*int(dimensions)+1,2):
  list_2.append('if random_var == ' + str(int(counter_2)) + ':\n var_' + str(int((int(counter_2) + 1)/2)) + ' = var_' + str(int((int(counter_2) + 1)/2)) + ' + 1')
 for counter_3 in range(2,2*int(dimensions)+1,2):
  list_3.append('if random_var == ' + str(int(counter_3)) + ':\n var_' + str(int((int(counter_3))/2)) + ' = var_' + str(int((int(counter_3) + 1)/2)) + ' - 1')
#Execution
 while True:
  random_var = random.randint(1, 2 * int(dimensions))
  for counter_4 in range(int(dimensions)):
   exec(list_2[counter_4])
   exec(list_3[counter_4])
  step = int(step) + 1
  if step == int(steps):
   break
  else:
   continue
#output
 for counter_5 in range(int(dimensions)):
  list_4.append('var_' + str(int(counter_5) + 1))
 for counter_6 in range(int(dimensions)):
  list_5.append(eval(list_4[int(counter_6)]))
 print('coordinates: ' + str(list_5))
