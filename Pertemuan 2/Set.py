#Set
warna = {"biru", "hitam", "hijau"}
print(warna)

#Tidak Boleh Duplikat
#Cth 1
warna = {"biru", "hitam", "hijau", "biru"}

print(warna)

#Cth 2
warna = {"biru", "hitam", "hijau", True, 1, 2}

print(warna)

#Set Item
warna = {"biru", "hitam", "hijau"}
angka = {1, 5, 7, 9, 3}
pernyataan = {True, False, False}

print(warna)
print(angka)
print(pernyataan)

#Akses item
# 1. for
warna = {"biru", "hitam", "hijau"}

for x in warna:
  print(x)

# 2. In
warna = {"biru", "hitam", "hijau"}

print("hitam" in warna)

#Tambahkan Item Baru
warna = {"biru", "hitam", "hijau"}

warna.add("merah")

print(warna)

#Tambahkan Set
warna1 = {"biru", "hitam", "hijau"}
warna2= {"ungu", "kuning", "abu"}

warna1.update(warna2)

print(warna1)

#Hapus Item Set
#remove()
warna = {"biru", "hitam", "hijau"}

warna.remove("hitam")

print(warna)

#discard()
warna = {"biru", "hitam", "hijau"}

warna.discard("hitam")

print(warna)

#pop()
warna = {"biru", "hitam", "hijau"}

x = warna.pop()
print(x)

print(warna)

#Frozenset
warna = frozenset({"biru", "hitam", "hijau"})
print(warna)
print(type(warna))

