import matplotlib.pyplot as plt
import numpy as np

x_1 = np.linspace(0,2 * np.pi, 6)
x_2 = np.linspace(0,2 * np.pi, 200)

plt.plot(x_1, np.sin(x_1), marker="o", label="6 titik")
plt.plot(x_2, np.sin(x_2), label = "200 titik")

plt.title("y = sin(x)")
plt.legend()
plt.show()
