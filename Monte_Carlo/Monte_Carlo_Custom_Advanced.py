#setup
import random
print('Welcome to my Monte Carlo simulation!')
while True:
 steps = int(input('How many steps? '))
 dimensions = input('How many dimensions? ')
 for counter_0 in range(int(dimensions)):
  exec('input_plus_' + str(int(counter_0) + 1) + ' = input(\'Probability of positive movement in dimension ' + str(int(counter_0) + 1) + ' (percentage) \')')
  exec('input_minus_' + str(int(counter_0) + 1) + ' = input(\'Probability of negative movement in dimension ' + str(int(counter_0) + 1) + ' (percentage) \')')
 alpha  =  False
 list_a =  []
 list_b =  []
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
 for counter_a in range(int(dimensions)):
  list_a.append(str((float(eval('input_plus_' + str((int(counter_a) + 1)))))/10))
  list_b.append(str((float(eval('input_minus_' + str((int(counter_a) + 1)))))/10))
#operations
 for counter_2 in range(int(dimensions)):
  list_2.append('if random_var < ' + str(" + ".join(list_a[0:counter_2 + 1] + list_b[0:counter_2])) + ': \n var_' + str(counter_2 + 1) + '= var_' + str(counter_2 + 1) + '+ 1')
 for counter_3 in range(int(dimensions)):
  list_3.append('if random_var < ' + str(" + ".join(list_a[0:counter_3 + 1] + list_b[0:counter_3 + 1])) + ': \n var_' + str(counter_3 + 1) + '= var_' + str(counter_3 + 1) + '- 1')
#execution
 while True:
  random_var = random.uniform(0, 10)
  for counter_4 in range(int(dimensions)):
   exec(list_2[counter_4] + '\n alpha = True')
   if alpha == True:
    alpha = False
    break
   exec(list_3[counter_4] + '\n alpha = True')
   if alpha == True:
    alpha = False
    break
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
