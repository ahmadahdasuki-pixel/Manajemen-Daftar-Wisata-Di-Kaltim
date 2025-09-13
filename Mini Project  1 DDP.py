#Manajemen Daftar Wisata Di Kaltim
print("-" * 60)
print("TEMA MINI PROJECT : Manajemen Daftar Wisata Di Kaltim")
print("NAMA  : Ahmad Ahdasuki")
print("NIM   : 2509116021")
print("KELAS : A Sistem Informasi")
print("TUGAS : Mini Project 1 Praktikum DDP ")
print("_" * 60)

#LIST DAFTAR WISATA, LOKASI, HARGA TIKET MASUK, JAM BUKA DAN TUTUP DI KALTIM
list_1 = ["Pulau Beras Basah, Bontang, 5000, 05:00-23:59"]
list_2 = ["Pantai Kemala, Samarinda, 10000, 07:00-21:00"]
list_3 = ["Danau Ubur-Ubur, Pulau Kakaban, 7000, 06:00-19:00"]
list_4 = ["Danau Labuan Cermin, Berau, 15000, 8:30-22:00"]
list_5 = ["Teluk Lerong Gerdon, Samarinda Ulu, 8000, 10:00-20:30"]


#MENU UTAMA
print("""
Tambah daftar wisata = 1
Menampilkan Daftar Wisata = 2
Mengganti salah satu tempat wisata = 3
Hapus Salah Satu Tempat Wisata = 4
Keluar Program = 5

""")

#INPUT PILIHAN MENU UTAMA
pilihan = int(input("Masukan pilihan menu ke berapa (1-5): "))

#CREATE(TAMBAH)
if pilihan == 1:
    nama = input("Masukan nama wisata baru: ")
    lokasi = input("Masukan Lokasi: ")
    harga_tiket = int(input("Masukan harga tiket: "))
    print(f"Wisata '{nama}', '{lokasi}', '{harga_tiket}'  Berhasil di Tambahkan")

#READ(MENAMPILKAN)
elif pilihan == 2:
        print("Daftar Wisata Kaltim")
        print(f"1, {list_1} ")
        print(f"2, {list_2} ")
        print(f"3, {list_3} ")
        print(f"4, {list_4} ")
        print(f"5, {list_5} ")

#UPDATE(MENGUBAH/MENGGANTI)
elif pilihan == 3:
    ganti = int(input("Masukkan nomor wisata yang ingin diganti (1-5): "))
    if ganti == 1:
        list_1 = [input("Masukkan data baru wisata 1: ")]
        print("Data berhasil diganti:", list_1)
    elif ganti == 2:
        list_2 = [input("Masukkan nama tempat baru wisata 2: ")]
        print("Data berhasil diganti:", list_2)
    elif ganti == 3:
        list_3 = [input("Masukkan nama tempat baru wisata 3: ")]
        print("Data berhasil diganti:", list_3)
    elif ganti == 4:
        list_4 = [input("Masukkan nama tempat baru wisata 4: ")]
        print("Data berhasil diganti:", list_4)
    elif ganti == 5:
        list_5 = [input("Masukkan nama tempat baru wisata 5: ")]
        print("Data berhasil diganti:", list_5)

#DELETE(MENGHAPUS)
elif pilihan == 4:
    hapus = int(input("Masukkan nomor wisata yang ingin dihapus (1-5): "))
    if hapus == 1:
        list_1 = ["Pulau Beras Basah, Bontang, 5000, 05:00-23:59"]
        print("Wisata 1 berhasil dihapus.")
    elif hapus == 2:
        list_2 = ["Pantai Kemala, Samarinda, 10000, 07:00-21:00"]
        print("Wisata 2 berhasil dihapus.")
    elif hapus == 3:
        list_3 = ["Danau Ubur-Ubur, Pulau Kakaban, 7000, 06:00-19:00"]
        print("Wisata 3 berhasil dihapus.")
    elif hapus == 4:
        list_4 = ["Danau Labuan Cermin, Berau, 15000, 8:30-22:00"]
        print("Wisata 4 berhasil dihapus.")
    elif hapus == 5:
        list_5 = ["Teluk Lerong Gerdon, Samarinda Ulu, 8000, 10:00-20:30"]
        print("Wisata 5 berhasil dihapus.")

#KELUAR
elif pilihan == 5:
    print("Program selesai, Terima kasih")

else:
    print("Pilihan anda tidak valid.")
