import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x), label='Sine')
plt.plot(x, np.cos(x), label='Cosine')
plt.plot(x, x**2, label='Polynomial (x^2)')
plt.plot(x, np.exp(x/2), label='Exponential')
plt.legend()
plt.show()