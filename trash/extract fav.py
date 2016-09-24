import os

list_fav = []
with open("fav.txt") as berkas:
	with open("hasil fav.txt", "w") as hasil_fav:
		list_berkas = berkas.read().splitlines()
		for n in range(len(list_berkas)):
			if list_berkas[n] == "f":
				list_fav.append(n + 1)
		hasil_fav.write(str(list_fav))
		os.system("subl 'hasil fav.txt'")