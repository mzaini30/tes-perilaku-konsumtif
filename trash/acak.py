import random, os

tanya_angka = int(raw_input("Masukkan jumlah angka yang mau diacak: "))
tanya_angka += 1

angka = range(1, tanya_angka)
random.shuffle(angka)
# print angka

with open("acak.txt", "w") as file_acak:
	for n in angka:
		file_acak.write(str(n)+"\n")
	os.system("subl acak.txt")