import numpy as np
import math
import matplotlib.pyplot as mpl

N = 77
a = 8
#you can change these values or take user input
z = list(range(N))
y = [a**z0 % N for z0 in z]

mpl.plot(z,y)
mpl.xlabel('z')
mpl.ylabel(f'{a}^z (mod {N})')
mpl.show()
r = z[y[1:].index(1)+1]
if r%2 == 0:
    x = (a**(r/2.)) % N
    if((x+1)%N != 0):
        print(math.gcd((int(x)+1),N), math.gcd((int(x)-1),N))
