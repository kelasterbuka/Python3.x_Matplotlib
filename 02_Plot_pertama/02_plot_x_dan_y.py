import matplotlib.pyplot as plt

# data lari

hari = [1,2,3,4,5,6,7]
jarak_km = [2.0,2.5,2.0,2.8,3.0,4.5,5.0]

# plt.plot(x,y)
plt.plot(hari,jarak_km)

# kita perlu memberi nama
plt.title("Lari pagi Ucup minggu ini")
plt.xlabel("Hari Ke-")
plt.ylabel("jarak (Km)")

plt.show()