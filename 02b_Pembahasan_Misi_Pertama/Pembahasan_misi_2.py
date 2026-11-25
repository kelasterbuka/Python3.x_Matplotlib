"""Belajar Matplotlib #2 · MISI UTAMA

Ucup sudah lari 14 hari. Ia ingin tahu: apakah ia benar-benar makin kuat,
atau cuma kebetulan ada beberapa hari yang bagus?

Tugasmu:
  1. Gambar garis jarak harian Ucup (sudah disiapkan).
  2. TODO: hitung RATA-RATA KUMULATIF: rata-rata dari hari 1 sampai hari ke-i.
     Petunjuk: np.cumsum(jarak) / hari
  3. TODO: gambar rata-rata kumulatif sebagai garis kedua dengan label.
  4. TODO: gambar garis target 4 km (garis datar) sebagai garis ketiga.
     Petunjuk: y-nya bisa dibuat dengan np.full(len(hari), 4.0)
  5. Tulis di komentar YouTube: di hari ke berapa rata-rata Ucup tembus 3 km?
"""

import matplotlib.pyplot as plt
import numpy as np

hari = np.arange(1,15)
jarak = np.array([2.0, 2.5, 2.3, 3.1, 3.0, 0.0, 3.6,
                  4.0, 3.5, 4.2, 0.0, 4.4, 4.1, 4.8])  # 0 = hari istirahat

# TODO 2: rata_kumulatif = ...
rata_kumulatif = np.cumsum(jarak)/hari

hari_lari = np.cumsum(jarak > 0)
rata_hari_lari = np.cumsum(jarak) / hari_lari

print("Rata-rata kumulatif hari ke-14: ", round(rata_kumulatif[-1],2))
print("Hari pertama rata-rata hari lari >= 3: ", hari[rata_hari_lari >=3][0])

# TODO 3: plt.plot(...)
plt.plot(hari, jarak, marker="o", label="jarak harian")
plt.plot(hari, rata_kumulatif, "bo:",linewidth=3, label="rata-rata kumulatif (istirahat = 0)")
plt.plot(hari, rata_hari_lari, "ro--",linewidth=3, label="rata-rata hari lari saja")

# TODO 4: plt.plot(...)
plt.plot(hari, np.full(len(hari),4.0), linestyle="--", color="gray", label="target 4 km")


plt.title("Lari pagi Ucup: 14 hari")
plt.xlabel("hari ke-")
plt.ylabel("jarak (km)")
plt.legend()
plt.show()
