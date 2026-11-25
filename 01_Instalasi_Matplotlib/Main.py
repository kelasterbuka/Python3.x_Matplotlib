import matplotlib
import matplotlib.pyplot as plt
import numpy

print("Matplotlib: ", matplotlib.__version__)
print("Numpy: ", numpy.__version__)

# testing membuat plot

fig, ax = plt.subplots(figsize=(6,3))
ax.text(0.5,0.5, "Matplotlib Uhuy!", ha="center",va="center",fontsize=20)
ax.set_axis_off()
plt.show()