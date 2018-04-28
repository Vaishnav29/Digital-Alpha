import numpy as np
import math
from sympy import *



def sigmoid(x):
    return 1/(1+math.exp(-x))


i =[0.05,0.10]
o=[0.01,0.99]
w=[0.15,.2,.25,.30,.40,.45,.5,.55]
b =[.35,.6]
c = o[0]
net_h1= w[0]*i[0]+w[1]*i[1]+b[0]

out_h1=sigmoid(net_h1)


net_h2= w[2]*i[0]+w[3]*i[1]+b[0]

out_h2=sigmoid(net_h2)


net_o1 = out_h1*w[4]+w[5]*out_h2+b[1]

out_o1= sigmoid(net_o1)
a=out_o1


net_o2 = out_h2*w[7]+w[6]*out_h1+b[1]

out_o2= sigmoid(net_o2)

Eo1 = ((out_o1-o[0])**2)/2
Eo2 = ((out_o2-o[1])**2)/2
Etot = Eo1+Eo2

from sympy import symbols, diff,solve
from sympy import Symbol,Derivative

out_o1 = Symbol('out_o1')
f = ((out_o1-o[0])**2)/2
deriv = Derivative(f,out_o1)
d=deriv.doit().subs({out_o1:a},{o[0]:c})



p1=1/(1+math.exp(-net_o1))
p2= p1*(1-p1)

net_o1, w[4] = symbols('net_o1 w[4]', real=True)
f = out_h1*w[4]+w[5]*out_h2+b[1]
p3 = diff(f, w[4])

