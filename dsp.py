import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
F=250;Fs=10000;
F1=200
s=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/2)
s1=2*np.cos(2*np.pi*F/Fs*n+np.pi/2)
s2=0.5*np.cos(2*np.pi*F/Fs*n+np.pi)
s3=0.5*np.cos(2*np.pi*F1/Fs*n+np.pi)
a=s+s1;
b=s+s2;
c=s+s3;
plt.subplot(4,2,1);
plt.stem(n,a);
plt.subplot(4,2,2);
plt.stem(n,s);
plt.subplot(4,2,3);
plt.stem(n,b);
plt.subplot(4,2,4);
plt.stem(n,c);
plt.show()

