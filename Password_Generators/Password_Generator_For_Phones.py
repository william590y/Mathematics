import string
import secrets
print('Welcome to my password generator!')
characters = list(string.digits)
while True:
 length = int(input('How long would you like your password? '))
 list = []
 for counter in range(length):
  list.append(secrets.choice(characters))
 print("".join(list))
