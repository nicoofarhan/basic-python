print("UJIAN MATEMATIKA")
print("================")

nilai_ujian_teori = int(input("MASUKKAN NILAI UJIAN TEORI ANDA = "))
nilai_ujian_praktek = int(input("MASUKKAN NILAI UJIAN PRAKTEK ANDA = "))

if (nilai_ujian_teori >= 70 and nilai_ujian_praktek >= 70):
    print("SELAMAT, ANDA LULUS UJIAN")
else:
    print("MAAF, ANDA HARUS MENGULANG UJIAN")