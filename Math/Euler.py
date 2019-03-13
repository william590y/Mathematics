import matplotlib.pyplot as plt
import requests
import decimal
import functools
def extract_pi(n):
    if n > 1000000 or n < 0:
        raise ValueError
    else:
        url = 'https://www.angio.net/pi/digits/pi1000000.txt'
        r = requests.get(url)
        digits = r.text
        if n == 1:
         output = 3
        else:
         output = float(digits[0:n])   
        return output
pi = extract_pi(1000000)

@functools.lru_cache()
def euler(n):
    if n == 1:
         return 1
    if n != 1:
         return euler(n-1) + 1/(n**2)
def euler_plot(n):
 x = list(range(n))
 y = []
 y2 = []
 for i in range(n):
  y.append(float(decimal.Decimal(euler(i+1)*6).sqrt()))
 for i in y:
  y2.append(pi-i)
 plt.plot(x,y2,label = 'Euler Approximation')
 plt.yscale('log')
 plt.title('Error Function') 
 plt.ylabel('Error')
 plt.xlabel('# of Terms')
 plt.legend()
 plt.show()
 
euler_plot(1000000)
