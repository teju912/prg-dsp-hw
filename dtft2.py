#dtft sinsoid
import numpy as np
from matplotlib import pyplot as plt
f=100
fs=250
m=np.arange(1,150)
x=np.cos(2*np.pi*f/fs*m)
w=np.arange(-np.pi,np.pi,0.001*np.pi);#(-pi to pi)
X=[]
for i in range(0,len(w)):
	l=len(x)
	c=0
	for n in range(0 ,(l)):
		c=c+x[n]*np.exp(-1*1j*w[i]*n)
	X.append(c)
plt.plot(w,np.abs(X))
plt.plot(w,np.angle(X))
plt.show()
