import numpy as np  
import matplotlib.pyplot as plt  

n = np.arange(0, 10)  
h_a = 1.2**n  

plt.stem(n, h_a)  
plt.title('h[n] = 1.2^n u[n]')  
plt.xlabel('n')  
plt.ylabel('h[n]')  
plt.grid()  
plt.show()