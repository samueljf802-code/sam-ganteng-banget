# Hewan = ["Kucing", "sapi", "kerbau"]
# print(Hewan[0])

# Hewan = ["kucing","sapi", "kerbau", "angsa", "singa"]
# print(Hewan[1:5])

# Hewan = ["kucing","sapi", "kerbau", "angsa", "singa"]
# print(Hewan[1:])

# Hewan = ["kucing","sapi", "kerbau", "angsa", "singa"]
# print(Hewan[:2])

# Hewan = ["kucing","sapi", "kerbau", "angsa", "singa"]
# print(Hewan[-3])

# Buah = ["apel", "mangga", "pisang"]
# Buah[2] = "nanas"
# print(Buah)

# Buah = ["apel", "mangga", "pisang", "kiwi"]
# Buah[2:4] = ["nanas", "semangka"]
# print(Buah)

# Buah = ["apel", "mangga", "pisang", "kiwi", "rambutan"]
# Buah[2:4] = ["nanas", "semangka"]
# print(Buah)

# Buah = ["apel", "mangga", "pisang"]
# Buah[1:3] = ["nanas"]
# print(Buah)

# Buah = ["apel", "mangga", "pisang"]
# Buah[1:3] = "nanas"
# print(Buah)

# Unggas = ["ayam", "bebek", "itik"]
# Unggas.append("angsa")
# print(Unggas)

# Unggas = ["ayam", "bebek", "itik"]
# Unggas.insert(1, "angsa")
# print(Unggas)

# Unggas = ["ayam", "bebek", "itik"]
# reptil = ["ular", ""]
# Unggas.extend("angsa")
# print(Unggas)

# list1 = [1, 2, 3, 4, 5] 
# list2 = ["a", "i", "u", "e", "o"]

# list1.extend(list2)

# print(list1)

# jumlah = input("Jumlah halaman: ")
# print("Nilai yang diterima:", jumlah)
# print("Tipe data:", type(jumlah))

# jumlah = int(input("Jumlah halaman: "))
# harga = int(input("Harga per halaman: "))
# subtotal = jumlah * harga
# print("Subtotal:", subtotal)

# jumlah_teks = "20"
# harga_teks = "500"

# jumlah = int(jumlah_teks)
# harga = int(harga_teks)
# subtotal = jumlah * harga

# # print("Subtotal:", subtotal)

# subtotal = 5000

# print(subtotal)
# print("Subtotal:", subtotal)

# nama_layanan = "Ganti oli mesin"
# subtotal = 10000

# print(f"{nama_layanan}: {subtotal}")

# print("7 + 3  =", 7 + 3)
# print("7 - 3  =", 7 - 3)
# print("7 * 3  =", 7 * 3)
# print("7 / 2  =", 7 / 2)
# print("7 // 2 =", 7 // 2)
# print("7 % 2  =", 7 % 2)
# print("2 ** 3 =", 2 ** 3)

# tanpa_kurung = 10000 + 5000 * 2
# dengan_kurung = (10000 + 5000) * 2

# print("Tanpa kurung:", tanpa_kurung)
# print("Dengan kurung:", dengan_kurung)

# def hitung_biaya_pencetakan(
#     halaman_bw,
#     harga_bw,
#     halaman_warna,
#     harga_warna,
#     biaya_jilid,
# ):
#     subtotal_bw = halaman_bw * harga_bw
#     subtotal_warna = halaman_warna * harga_warna
#     total_biaya = subtotal_bw + subtotal_warna + biaya_jilid

#     return {
#         "subtotal_bw": subtotal_bw,
#         "subtotal_warna": subtotal_warna,
#         "total_biaya": total_biaya,
#     }

# jumlah_teks = "20"
# harga_teks = "500"

# jumlah = int(jumlah_teks)
# harga = int(harga_teks)
# subtotal = jumlah * harga

# print("Subtotal:", subtotal)

# makanan = ("soto", "seblak", "ramen")
# print(makanan[0:2])

# Mahasiswa = ("Janson", "Dapid", "Megawati", "janggar")
# Mahasiswa2




# Buah1 = ["Nanas", "Apel", "Mangga"]
# buah2 = list(Buah1)
# buah2.append("Jeruk")
# Buah = tuple(buah2)
# print(Buah)

# Kendaraan = ["Mobil", "Motor", "Sepeda"]
# (Merah, Hitam, Biru) = Kendaraan
# print(Merah)
# print(Hitam)
# print(Biru)

# makanan = ("Soto", "ayam geprek", "bebek goreng")
# daftar = makanan * 2
# print(daftar)

# nama = ("Nama saya udin din din bin udin")
# hitung = nama.index('n')
# print(hitung)

# Unggas = ["ayam", "bebek", "itik"]
# Reptil = ["ular", "kadal"]
# Unggas.update(Reptil)
# print(Unggas)

# Makanan = {"Soto", "Seblak", "Ramen"}
# for x in Makanan:
#    print(x)

# huruf = {"a", "b", "c"}
# angka = {1, 2, 3}
# gabungan = huruf.union(angka)
# print(gabungan)

# x = frozenset({"apel", "pisang", "ceri"})
# print(x)
# print(type(x))

# Mobil = {
# "brand": "Ford", "model": "Mustang", "tahun": 1964}
# Mobil["tahun"] = 2018
# print(Mobil["tahun"])

# Mobil = {
# "brand": "Ford",
# "model": "Mustang",
# "tahun": 1964
# }
# Mobil.update({"tahun": 2020})
# print(Mobil["tahun"])

# Mobil = {
# "brand": "Ford",
# "model": "Mustang",
# "tahun": 1964
# }
# Mobil.update({"warna": "merah"})
# print(Mobil)

# Mobil = {
# "brand": "Ford",
# "model": "Mustang",
# "tahun": 1964
# }

# Mahasiswa1 = {
# "nama" : "Emil",
# "lahir" : 2004
# }
# Mahasiswa2 = {
# "nama" : "Tobias",
# "lahir" : 2007
# }
# Mahasiswa3 = {
# "nama" : "Linus",
# "lahir" : 2011
# }
# Himpunan = {
# "Mahasiswa1" : Mahasiswa1,
# "Mahasiswa2" : Mahasiswa2,
# "Mahasiswa3" : Mahasiswa3
# }
# print(Himpunan["Mahasiswa2"]["nama"])

# try:
#     nilai = int("dua")
# except ValueError as error:
#     print("ValueError:", error)

# data_uji = [
#     ((20, 500, 5, 2000, 8000), 28000),
#     ((0, 500, 10, 2000, 0), 20000),
#     ((1, 500, 0, 2000, 8000), 8500),
# ]

# for parameter, expected in data_uji:
#     actual = (def "hitung_biaya_pencetakan"(*parameter) ) ["total_biaya"]
#     status = "LULUS" if actual == expected else "GAGAL"
#     print(f"input={parameter} expected={expected} actual={actual} -> {status}")
#     assert actual == expected

# print("Semua data uji lulus.")


# saldo = 75000
# nilai_transaksi = 80000

# if saldo >= nilai_transaksi:
#     print("Transaksi diproses.")
# else:
#     print("Transaksi ditolak: saldo tidak mencukupi.")

# def seleksi_beasiswa(nama, nilai, kehadiran):
#     if nilai >= 85 and kehadiran >= 90:
#         return "LOLOS"
#     elif nilai >= 75 and kehadiran >= 80:
#         return "DIPERTIMBANGKAN"
#     else:
#         return "TIDAK LOLOS"


# print("=== SELEKSI BEASISWA ===")

# lanjut = "y"
# while lanjut == "y":
#     print()
#     nama = input("Nama peserta: ")
#     nilai = float(input("Nilai akademik: "))
#     kehadiran = float(input("Kehadiran (%): "))

#     hasil = seleksi_beasiswa(nama, nilai, kehadiran)

#     print()
#     print("Nama      :", nama)
#     print("Nilai     :", nilai)
#     print("Kehadiran :", str(kehadiran) + "%")
#     if hasil == "LOLOS":
#         print("Hasil:", nama, "dinyatakan LOLOS")
#     elif hasil == "DIPERTIMBANGKAN":
#         print("Hasil:", nama, "DIPERTIMBANGKAN")
#     else:
#         print("Hasil:", nama, "dinyatakan TIDAK LOLOS")

#     print()
#     lanjut = input("Tambah peserta? (y/n): ").lower()

# print()
# print("Program selesai.")

# def tentukan_kategori(nilai):
#     if nilai >= 85:
#         return "A"
#     elif nilai >= 70:
#         return "B"
#     elif nilai >= 60:
#         return "C"
#     else:
#         return "D"


# # 1. Baca jumlah mahasiswa, validasi > 0 dengan while
# jumlah_mhs = int(input("Jumlah mahasiswa: "))
# while jumlah_mhs <= 0:
#     print("Jumlah harus lebih dari 0!")
#     jumlah_mhs = int(input("Jumlah mahasiswa: "))

# total = 0          # accumulator
# lulus = 0          # counter lulus (A, B, C)
# tidak_lulus = 0    # counter tidak lulus (D)

# # 2. Baca setiap nilai dengan for
# for i in range(1, jumlah_mhs + 1):
#     nilai = float(input(f"Nilai mahasiswa ke-{i}: "))

#     # 3. Validasi nilai harus 0-100
#     while nilai < 0 or nilai > 100:
#         print("Nilai harus antara 0 dan 100!")
#         nilai = float(input(f"Nilai mahasiswa ke-{i}: "))

#     # 4. Panggil fungsi dan tampilkan kategori
#     kategori = tentukan_kategori(nilai)
#     print("Kategori:", kategori)

#     # 5. Accumulator total nilai
#     total = total + nilai

#     # 6. Counter lulus / tidak lulus
#     if kategori == "A" or kategori == "B" or kategori == "C":
#         lulus = lulus + 1
#     else:
#         tidak_lulus = tidak_lulus + 1

# # 7. Tampilkan hasil
# rata_rata = total / jumlah_mhs
# print("Rata-rata:", rata_rata)
# print("Lulus:", lulus, "| Tidak lulus:", tidak_lulus)