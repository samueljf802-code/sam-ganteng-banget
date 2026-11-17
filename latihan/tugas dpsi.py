print("=" * 52)
print("        Kalkulator Penghitungan Gaji")
print("=" * 52)

try:
    nama = input("Masukkan nama pegawai: ")
    lama_kerja = int(input("Masukkan lama bekerja (bulan): "))
    gaji_pokok = float(input("Masukkan gaji pokok: "))

    if lama_kerja < 0 or gaji_pokok < 0:
        raise ValueError

    if lama_kerja >= 24:
        persen_bonus = 0.25
    elif lama_kerja >= 12:
        persen_bonus = 0.15
    else:
        persen_bonus = 0

    bonus = gaji_pokok * persen_bonus
    total_gaji = gaji_pokok + bonus

    print("-" * 52)
    print(f"Bonus yang anda dapatkan sebanyak: {bonus}")
    print("-" * 52)
    print(f"Total penghitungan gaji anda adalah: {total_gaji}")

except ValueError:
    print("Inputan yang Anda masukkan tidak valid")