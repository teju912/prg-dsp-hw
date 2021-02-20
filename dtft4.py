#dtft sinsoid x+noise
import numpy as np
import scipy.io.wavfile
from matplotlib import pyplot as plt
f=100
fs=1000
fs,x=scipy.io.wavfile.read('janu.wav')
print(fs)
x=x[:,0]
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
print(x.shape)
