#dtft sinsoid
import numpy as np
from matplotlib import pyplot as plt
x=np.random.rand(500)
x=x-np.sum(x)
w=np.arange(-np.pi,np.pi,0.001*np.pi);#(-pi to pi)
X=[]
for i in range(0,len(w)):
	l=len(x)
	c=0
	for n in range(0 ,(l)):
		c=c+x[n]*np.exp(-1*1j*w[i]*n)
	X.append(c)
plt.stem(w,np.abs(X))
plt.stem(w,np.angle(X))
plt.show()
