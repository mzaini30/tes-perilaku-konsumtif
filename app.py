def garis():
	print "-" * 80

banyak_opsi = 4
def ubah_fav(x):
	jawaban[x] = banyak_opsi + 1 - int(jawaban[x])

fav = [2, 3, 4, 6, 8, 11, 14, 16, 19, 20, 22, 23]
for n in range(len(fav)):
	fav[n] = fav[n] - 1

pilihan = """1. Sangat setuju
2. Setuju
3. Tidak setuju
4. Sangat tidak setuju"""

with open("pernyataan.txt") as pernyataan:
	list_pernyataan = pernyataan.read().splitlines()

jawaban = []
for n in list_pernyataan:
	garis()
	print n
	garis()
	print pilihan
	garis()
	jawaban.append(raw_input("Masukkan jawabanmu: "))
for n in range(len(fav)):
	ubah_fav(fav[n])
jumlah = 0
for n in jawaban:
	n = int(n)
	jumlah += n

"""
1-24
25-48
49-72
73-96
"""

garis()
print "Tingkatan konsumtif kamu %r dari 96" % jumlah

konsumtif_banget = """Wah, kamu ternyata konsumtif banget!
Hati-hati lo, ntar sebelum akhir bulan, duitmu habis duluan
Mulai sekarang, belajar nabung ya..."""
agak_konsumtif = """Bentar lagi kamu bisa jadi orang yang konsumtif banget lo..
Ingat ya, selalu atur pola belanjamu supaya nggak kebablasan"""
agak_hemat = """Tetap berjuang mengatur pola konsumsimu ya...
Kamu sudah hebat tu, bisa mengatur keuangan..."""
hemat_banget = """Selamat, kamu sudah bisa mengendalikan kebiasaan belanjamu
Kamu sudah bisa mengatur keuanganmu"""

garis()
if 1 <= jumlah <= 24:
	print hemat_banget
elif 25 <= jumlah <= 48:
	print agak_hemat
elif 49 <= jumlah <= 72:
	print agak_konsumtif
elif 73 <= jumlah <= 96:
	print konsumtif_banget
garis()