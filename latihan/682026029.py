nilai = [78, 90, 65, 82, 75]

cari = int(input("Masukkan nilai yang dicari: "))

ketemu = False
for i in range(len(nilai)):
    if nilai[i] == cari:
        print(f"Nilai ditemukan pada index {i}")
        ketemu = True
        break

if not ketemu:
    print("Nilai tidak ditemukan")


nilai = [78, 90, 65, 82, 75]

print("Sebelum diurutkan:", nilai)

n = len(nilai)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if nilai[j] > nilai[j + 1]:
            nilai[j], nilai[j + 1] = nilai[j + 1], nilai[j]

print("Sesudah diurutkan:", nilai)

barang = [
    {"kode": "ATK-01", "nama": "Buku", "stok": 12},
    {"kode": "ATK-02", "nama": "Pensil", "stok": 20},
    {"kode": "ATK-03", "nama": "Penggaris", "stok": 8},
]

kode = input("Masukkan kode barang: ")

ketemu = False
for item in barang:
    if item["kode"] == kode:
        print(f"Nama: {item['nama']}, Stok: {item['stok']}")
        ketemu = True
        break

if not ketemu:
    print("Kode tidak ditemukan")


subtotal = float(input("Masukkan subtotal belanja: "))
if subtotal >= 100000:
    diskon = subtotal * 0.10
else:
    diskon = 0

total = subtotal - diskon
print(f"Diskon: {diskon}")
print(f"Total dibayar: {total}")

total_harga = 50000
jumlah_barang = int(input("Jumlah barang: "))

total_harga = 50000
jumlah_barang = int(input("Jumlah barang: "))

if jumlah_barang > 0:
    rata_rata = total_harga / jumlah_barang
    print("Rata-rata harga:", rata_rata)
else:
    print("Jumlah barang harus lebih dari 0")