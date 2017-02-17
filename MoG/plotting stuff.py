import matplotlib.pyplot as plt
import numpy as plt

plt.plot([0.001,0.005,0.05,0.01,0.1,1.0], [0.98334,0.49237,0.38740,0.56579,0.85699,1.86245], 'bo')
plt.plot([0.001,0.005,0.05,0.01,0.1,1.0], [1.01839,0.97814,0.95633,1.30734,1.14380 ,1.86104], 'go')
plt.axis([0, 1, 0, 5])
plt.title('Cross-Entropy for different Learning Rates $\epsilon$')
plt.show()
