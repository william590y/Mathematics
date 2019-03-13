while True:
#Initialization
 n = 3
 k = 1
 primes = {2}
#Welcome
 limit = int(input('How many primes? '))
 print('Prime Numbers')
 print(2)
#Process
 while True:
  if k == limit:
   break
  try:
   for counter in primes:
    if n%counter == 0:
     raise MemoryError
    else:
     continue
   primes.add(n)
   print(n)
   n = n + 1
   k = k + 1
  except MemoryError:
   n = n + 1
