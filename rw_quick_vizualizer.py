import random
from numpy import pi, sin, cos, zeros
from matplotlib import pyplot as plt

alpha=2.0
sims=1000
x=zeros(sims)
y=zeros(sims)

for i in range(1, sims):
    theta = random.random()*2.*pi
    f = (1-random.random())**(-1./alpha)
    x[i] = x[i-1] + f*cos(theta)
    y[i] = y[i-1] + f*sin(theta)

plt.plot(x,y)
plt.show()
