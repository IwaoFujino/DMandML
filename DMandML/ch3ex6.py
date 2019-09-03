# sin()関数とcos()関数のグラフ
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 2, 0.01)
xpi=x*np.pi
sinx=np.sin(xpi)
cosx=np.cos(xpi)

plt.title("sine function and cosine function")
plt.xlabel("rad(×$\pi$)")
plt.grid(True)
plt.plot(x,sinx, label="sin(x)")
plt.plot(x,cosx, label="cos(x)")
plt.legend()
plt.show()
