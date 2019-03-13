from sympy.stats import *
from sympy import *
import matplotlib.pyplot as plt
x,y,z,h,t,tau,e,i = symbols('x y z h t tau e i')
init_printing()
from IPython.display import display
f1 = sympify(input()).subs({e:E,i:I})
g1 = sympify(input()).subs({e:E,i:I})
g=g1.subs(t,tau)
f = f1.subs({t:(t-tau)})
h1=Integral(g*f,(tau,0,t))
display(h1)
h=h1.doit()
if h == h1:
    print('No Elementary Solution')
else:
 display(simplify(h))
 try:
  p = plot(f1,g1,h,show = False)
  p[0].line_color = 'r'
  p[1].line_color = 'g'
  p.show()
 except:
    print('Graph Unavailable')