import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,.1)
y = x* np.sin(x)

plt.plot(x,y,'k+')
plt.xlabel('lado x')
plt.ylabel('lado y')
plt.title('y vs. x')
plt.show()
