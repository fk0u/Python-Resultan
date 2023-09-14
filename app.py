import math
import matplotlib.pyplot as plt

# Fungsi untuk menghitung resultan vektor
def hitung_resultan(vektor1, vektor2):
    x1, y1 = vektor1
    x2, y2 = vektor2
    resultan_x = x1 + x2
    resultan_y = y1 + y2
    resultan = math.sqrt(resultan_x**2 + resultan_y**2)
    return resultan, (resultan_x, resultan_y)

# Input vektor pertama
x1 = float(input("Masukkan komponen x dari vektor pertama: "))
y1 = float(input("Masukkan komponen y dari vektor pertama: "))
vektor1 = (x1, y1)

# Input vektor kedua
x2 = float(input("Masukkan komponen x dari vektor kedua: "))
y2 = float(input("Masukkan komponen y dari vektor kedua: "))
vektor2 = (x2, y2)

# Hitung resultan vektor
resultan, resultan_vektor = hitung_resultan(vektor1, vektor2)

# Menampilkan hasil
print(f"Resultan vektor: {resultan}")
print(f"Komponen x resultan vektor: {resultan_vektor[0]}")
print(f"Komponen y resultan vektor: {resultan_vektor[1]}")

# Membuat plot untuk vektor
plt.figure()
plt.quiver(0, 0, vektor1[0], vektor1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vektor 1')
plt.quiver(0, 0, vektor2[0], vektor2[1], angles='xy', scale_units='xy', scale=1, color='g', label='Vektor 2')
plt.quiver(0, 0, resultan_vektor[0], resultan_vektor[1], angles='xy', scale_units='xy', scale=1, color='b', label='Resultan')
plt.xlim(-abs(resultan), abs(resultan))
plt.ylim(-abs(resultan), abs(resultan))
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid()
plt.show()
