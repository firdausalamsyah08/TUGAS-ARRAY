inventaris = []

# Fungsi untuk menginput data barang
def input_barang():
    nama = input("Masukkan nama barang: ")
    kode = input("Masukkan kode barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    data_barang = {
        'nama': nama,
        'kode': kode,
        'jumlah': jumlah
    }
    inventaris.append(data_barang)
    print("Barang berhasil ditambahkan!")

# Fungsi untuk menampilkan semua barang
def tampilkan_barang():
    if not inventaris:
        print("Tidak ada data barang yang tersedia.")
        return
    print("Daftar Inventaris Barang:")
    for i, barang in enumerate(inventaris):
        print(f"Barang {i + 1}:")
        print(f"  Nama: {barang['nama']}")
        print(f"  Kode: {barang['kode']}")
        print(f"  Jumlah: {barang['jumlah']}")
        print("-" * 20)

# Fungsi untuk mencari barang berdasarkan kode
def cari_barang_kode():
    kode = input("Masukkan kode barang yang dicari: ")
    for barang in inventaris:
        if barang['kode'] == kode:
            print("Barang ditemukan:")
            print(f"  Nama: {barang['nama']}")
            print(f"  Kode: {barang['kode']}")
            print(f"  Jumlah: {barang['jumlah']}")
            return
    print("Barang dengan kode tersebut tidak ditemukan.")

# Fungsi untuk menghapus barang berdasarkan kode
def hapus_barang_kode():
    kode = input("Masukkan kode barang yang ingin dihapus: ")
    for barang in inventaris:
        if barang['kode'] == kode:
            inventaris.remove(barang)
            print("Barang berhasil dihapus!")
            return
    print("Barang dengan kode tersebut tidak ditemukan.")

# Program utama
def main():
    while True:
        print("\nManajemen Data Inventaris Barang")
        print("1. Tambah barang")
        print("2. Tampilkan semua barang")
        print("3. Cari barang berdasarkan kode")
        print("4. Hapus barang berdasarkan kode")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            input_barang()
        elif pilihan == '2':
            tampilkan_barang()
        elif pilihan == '3':
            cari_barang_kode()
        elif pilihan == '4':
            hapus_barang_kode()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
