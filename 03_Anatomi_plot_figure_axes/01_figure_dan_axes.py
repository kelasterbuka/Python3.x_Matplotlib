import matplotlib.pyplot as plt

hari = [1, 2, 3, 4, 5, 6, 7]
jarak_km = [2.0, 2.5, 2.3, 3.1, 3.0, 3.6, 4.0]

fig, ax = plt.subplots()

ax.plot(hari,jarak_km, marker ="o")
ax.set_title("Lari pagi Ucup")
ax.set_xlabel("hari ke-")
ax.set_ylabel("jarak (km)")

print(type(fig))
print(type(ax))

plt.show()