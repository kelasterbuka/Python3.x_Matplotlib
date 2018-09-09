import matplotlib.pyplot as plt
import numpy as np

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,theta):
	t = np.arange(0,tAkhir,0.1)
	y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
	return t,y

t,y = sinusGenerator(1,1,4,0)


# membuat plot
plt.plot(t,y)

# setting axis, minimum sama maximum
plt.axis([0,4,-2,2])

# menampilkan
plt.show()