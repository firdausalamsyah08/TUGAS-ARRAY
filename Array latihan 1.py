mahasiswa = []

# Fungsi untuk menginput data mahasiswa
def input_mahasiswa():
    nama = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    prodi = input("Masukkan program studi mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa = {
        'nama': nama,
        'nim': nim,
        'prodi': prodi,
        'nilai': nilai
    }
    mahasiswa.append(data_mahasiswa)

# Fungsi untuk menampilkan data mahasiswa
def tampilkan_mahasiswa():
    if not mahasiswa:
        print("Tidak ada data mahasiswa yang tersedia.")
        return
    for i, mhs in enumerate(mahasiswa):
        print(f"Mahasiswa {i + 1}:")
        print(f"  Nama: {mhs['nama']}")
        print(f"  NIM: {mhs['nim']}")
        print(f"  Program Studi: {mhs['prodi']}")
        print(f"  Nilai: {mhs['nilai']}")
        print("-" * 20)

# menghitung dan menampilkan rata-rata nilai mahasiswa
def tampilkan_rata_rata_nilai():
    if not mahasiswa:
        print("Tidak ada data mahasiswa untuk menghitung rata-rata.")
        return
    total_nilai = sum(mhs['nilai'] for mhs in mahasiswa)
    rata_rata_nilai = total_nilai / len(mahasiswa)
    print(f"Rata-rata Nilai: {rata_rata_nilai:.2f}")
    return rata_rata_nilai

# mencari dan menampilkan mahasiswa nilai tertinggi dan terendah
def tampilkan_nilai_tertinggi_terendah():
    if not mahasiswa:
        print("Tidak ada data mahasiswa untuk mencari nilai tertinggi dan terendah.")
        return None, None
    tertinggi = max(mahasiswa, key=lambda m: m['nilai'])
    terendah = min(mahasiswa, key=lambda m: m['nilai'])
    print(f"Nilai Tertinggi: {tertinggi['nilai']} (Mahasiswa: {tertinggi['nama']})")
    print(f"Nilai Terendah: {terendah['nilai']} (Mahasiswa: {terendah['nama']})")
    return tertinggi, terendah

# menampilkan ringkasan data
def tampilkan_ringkasan():
    print("\nRingkasan Data Mahasiswa:")
    if mahasiswa:
        rata_rata_nilai = tampilkan_rata_rata_nilai()
        tertinggi, terendah = tampilkan_nilai_tertinggi_terendah()
        for mhs in mahasiswa:
            print(f"Nama Mahasiswa : {mhs['nama']}, NIM Mahasiswa : {mhs['nim']}")
        print(f"\nRata-rata Nilai: {rata_rata_nilai:.2f}")
        if tertinggi and terendah:
            print(f"Mahasiswa dengan Nilai Tertinggi: {tertinggi['nama']} (NIM: {tertinggi['nim']})")
            print(f"Mahasiswa dengan Nilai Terendah: {terendah['nama']} (NIM: {terendah['nim']})")
    else:
        print("Tidak ada data mahasiswa yang tersedia.")

# Program utama
def main():
    while True:
        print("\nManajemen Data Mahasiswa")
        print("1. Input data mahasiswa")
        print("2. Tampilkan data mahasiswa")
        print("3. Tampilkan rata-rata nilai")
        print("4. Tampilkan mahasiswa dengan nilai tertinggi dan terendah")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            input_mahasiswa()
        elif pilihan == '2':
            tampilkan_mahasiswa()
            tampilkan_ringkasan()
            break
        elif pilihan == '3':
            tampilkan_rata_rata_nilai()
            tampilkan_ringkasan()
            break
        elif pilihan == '4':
            tampilkan_nilai_tertinggi_terendah()
            tampilkan_ringkasan()
            break
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
