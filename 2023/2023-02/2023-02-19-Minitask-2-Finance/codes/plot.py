import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt("result.csv", delimiter=',')
data

plt.figure()
plt.plot(data[:, 0], data[:, 1], label="P(r, t, T)")
plt.plot(data[:, 0], data[:, 2], label="V(r, t, T)")
plt.legend()
plt.title("P, V - r (Xr=0.05, r=0.0625, t=0, T=6)")
plt.xlabel("r")
plt.ylabel("V(r, t, T)")
plt.show()