transaksi = []

#menginput transaksi
def input_transaksi():
    jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
    if jenis not in ["pemasukan", "pengeluaran"]:
        print("Jenis transaksi tidak valid. Harus 'pemasukan' atau 'pengeluaran'.")
        return
    keterangan = input("Masukkan keterangan transaksi: ")
    jumlah = float(input("Masukkan jumlah transaksi: "))
    data_transaksi = {
        'jenis': jenis,
        'keterangan': keterangan,
        'jumlah': jumlah
    }
    transaksi.append(data_transaksi)
    print("Transaksi berhasil ditambahkan!")

#menampilkan semua transaksi
def tampilkan_transaksi():
    if not transaksi:
        print("Tidak ada data transaksi yang tersedia.")
        return
    print("Daftar Transaksi:")
    for i, tr in enumerate(transaksi):
        print(f"Transaksi {i + 1}:")
        print(f"  Jenis: {tr['jenis']}")
        print(f"  Keterangan: {tr['keterangan']}")
        print(f"  Jumlah: {tr['jumlah']}")
        print("-" * 20)

#total pemasukan
def total_pemasukan():
    total = sum(tr['jumlah'] for tr in transaksi if tr['jenis'] == 'pemasukan')
    print(f"Total Pemasukan: {total:.2f}")
    return total

#nampilin total pengeluaran
def total_pengeluaran():
    total = sum(tr['jumlah'] for tr in transaksi if tr['jenis'] == 'pengeluaran')
    print(f"Total Pengeluaran: {total:.2f}")
    return total

#saldo akhir
def saldo_akhir():
    pemasukan = total_pemasukan()
    pengeluaran = total_pengeluaran()
    saldo = pemasukan - pengeluaran
    print(f"Saldo Akhir: {saldo:.2f}")
    return saldo

# Program inti
def main():
    while True:
        print("\nManajemen Keuangan Pribadi")
        print("1. Tambah transaksi")
        print("2. Tampilkan semua transaksi")
        print("3. Tampilkan total pemasukan")
        print("4. Tampilkan total pengeluaran")
        print("5. Tampilkan saldo akhir")
        print("6. Keluar")
        pilihan = input("Masukkan pilihan Anda: ")
        
        if pilihan == '1':
            input_transaksi()
        elif pilihan == '2':
            tampilkan_transaksi()
        elif pilihan == '3':
            total_pemasukan()
        elif pilihan == '4':
            total_pengeluaran()
        elif pilihan == '5':
            saldo_akhir()
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
