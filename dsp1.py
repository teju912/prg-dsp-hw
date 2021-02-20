import numpy as np
from matplotlib import pyplot as plt
n=np.arange(0,500)
F=250;Fs=10000;
s=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/2)
s1=0.5*np.cos(2*np.pi*F/Fs*n+np.pi)
a=s+s1;
plt.stem(n,a);
plt.show()
