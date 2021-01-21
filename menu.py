def menu():
    print("===Menu===")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")
    print(" ")

def kontak():
    names = len(NamaKontak)
    for i in range(names):
        print("Nama: {}".format(NamaKontak[i]))
        print("No Telepon: {}".format(Nomor[i]))
print("SELAMAT DATANG!")
menu()
def kontak():
    print(" ")
    if pilih == 1:
        print("Daftar Kontak")
        kontak()
        print("\n")
        if len(NamaKontak) == 0:
            print("Kontak belum tersedia")
            print("\n")
        else:
            kontak()
            print("\n")
        menu()
    elif pilih == 2:
        print("Tambahkan Kontak")
        Nama = input("Masukkan nama: ")
        No = input("Masukkan nomor telepon: ")

        kontaknum["Nama :"] = Nama
        kontaknum["No Telepon :"] = No
        Nama = input("Masukkan Nama: ")
        No = input("Masukkan No Telepon: ")

        NamaKontak.append(Nama)
        Nomor.append(No)

        print("Kontak berhasil ditambahkan")
        print("\n")
        menu()
    elif pilih > 3:
        print("Menu tidak tersedia")
        print("\n")
        menu()
    pilih = int(input("Pilih menu: "))
print(" ")
print("Selesai, Terima Kasih!")