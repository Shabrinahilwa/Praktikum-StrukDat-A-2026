#Tuple
hewan = ("kucing", "monyet", "kelinci")
print(hewan)

#izinkan Duplikat
hewan = ("kucing", "monyet", "kelinci", "kucing", "anjing")
print(hewan)

#Buat Tuple dengan Satu Item
hewan = ("kucing",)
print(type(hewan))

hewan = ("monyet")   #NOT a tuple
print(type(hewan))

#Konstruktor tuple()
hewan = tuple(("kucing", "monyet", "kelinci"))
print(hewan)

#Mengubah Nilai Tuple
x = ("kucing", "monyet", "kelinci")
y = list(x)
y[1] = "anjing"
x = tuple(y)

print(x)

#Tambah Item
# 1. Konversi menjadi daftar
hewan = ("kucing", "monyet", "kelinci")
y = list(hewan)
y.append("tupai")
hewan = tuple(y)

print(hewan)

# 2. Menambahkan Tuple ke Tuple
hewan = ("kucing", "monyet", "kelinci")
y = ("tupai",)
hewan += y

print(hewan)

#Unpacking Tuple
hewan = ("kucing", "monyet", "kelinci")

(putih, coklat, abu) = hewan

print(putih)
print(coklat)
print(abu)

#Menggunakn Asterisk *
hewan = ("kucing", "monyet", "kelinci", "tupai", "anjing")

(putih, coklat, *abu) = hewan

print(putih)
print(coklat)
print(abu)

#Gabungan Dua Tuple
huruf = ("a", "b" , "c")
angka = (1, 2, 3)

gabungan = huruf + angka
print(gabungan)

#Mengalikan Tuple
hewan = ("kucing", "monyet", "kelinci")
mytuple = hewan * 2

print(mytuple)