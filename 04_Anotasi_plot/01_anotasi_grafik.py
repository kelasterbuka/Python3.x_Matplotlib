import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 3.5, 50)
y1 = 3 + np.cos(x)
y2 = 1 + np.sin(x) * 0.8

fig, ax = plt.subplots(figsize=(10,7),facecolor="#bdbdbcf9")

fig.subplots_adjust(left=0.15, right=0.8, top=0.86, bottom=0.19)

ax.plot(x,y1, color="tab:blue", linewidth=2.5, label="garis biru")
ax.plot(x[::5],y2[::5], "s", color ="tab:orange", markersize=8, label="titik oranye")

ax.set_xlim(0,4)
ax.set_ylim(0,4.5)

ax.set_title("Plot sinusoidal",fontsize=14)
ax.set_xlabel("Label sumbu x (xlabel)")
ax.set_ylabel("Label sumbu y (ylabel)")

ax.grid(linestyle=":")

ax.legend(loc="upper right")

# ANOTASI
# ax.annotate(tulisan, posisi, koordinat, xytext)

def tunjuk(text_data, pos_tunjuk, pos_text, warna_panah):
	ax.annotate(text_data, 
		xy = pos_tunjuk, 
		xytext = pos_text, 
		arrowprops=dict(
			arrowstyle="->",
			color=warna_panah,
			linewidth=1.5)
		)

tunjuk("garis",(1.5,3+np.cos(1.5)),(1.0,4.0),"red")
tunjuk("kotak",(x[25],y2[25]),(1.5,1.0),"blue")





plt.show()