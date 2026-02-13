#List
warna = ["merah", "hitam", "biru"]
print(warna)

#Allow Duplicates
warna = ["kuning", "hijau", "abu", "hijau", "kuning"]
print(warna)

#Panjang List
warna = ["merah", "hitam", "biru"]
print(len(warna))

#Item List
warna = ["merah", "hitam", "biru"]
angka = [1, 5, 7, 9, 3]
pernyataan = [True, False, False]

print(warna)
print(angka)
print(pernyataan)

#Contain Different Data Types
mylist= ["abc", 34, True, 40, "male"]

print(mylist)

#Type()
mylist = ["abu", "45", "false"]
print(type(mylist))

#Mengakses Item
buah = ["pisang", "anggur", "jeruk"]
print(buah[1])

#Pengindesian Negatif
buah = ["pisang", "anggur", "jeruk"]
print(buah[-1])

#Rentang Index
hewan = ["kucing", "anjing", "kelinci", "harimau", 
        "gajah", "singa", "zebra"]
print(hewan[2:5])

#Rentang dimulai dari Item Pertama
hewan = ["kucing", "anjing", "kelinci", "harimau", 
        "gajah", "singa", "zebra"]
print(hewan[:4])

#menghilangkan nilai akhir
fruits = ["apple", "banana", "cherry", "orange",
        "kiwi", "melon", "mango"]
print(buah[2:])

#Rentang Index Negatif
fruits = ["apple", "banana", "cherry", "orange", 
        "kiwi", "melon", "mango"]
print(buah[-4:-1])

#Periksa Item
warna = ["kuning", "hijau", "abu",]
if "hijau" in warna:
  print("Iya, 'hijau' ada dalam list warna")

#Ubah Nilai Item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blackcurrant"
print(fruits)

#Rubah rentang nilai item
buah = ["apel", "pisang", "ceri", "jeruk", "kiwi"]
buah[1:3] = ["mangga", "semangka"]
print(buah)

#Sisipkan Item
buah = ["apel", "pisang", "ceri",]
buah.insert(2, "jeruk")
print(buah)

#Tambahkan Item
warna = ["kuning", "hijau", "abu",]
warna.append("pink")
print(warna)

#Perluas List
angka_1 = [2, 4 ,6 ,8]
angka_2 = [1, 3, 5, 7]
angka_1.extend(angka_2)
print(angka_1)

#Hapus Item yang Ditentukan
barang = ["sendal", "sepatu", "sapu"]
barang.remove("sapu")
print(barang)

#Hapus Indeks yang Ditentukan
color = ["red", "yellow", "blue"]
color.pop(1)
print(color)

#Pop tidak tentukan index
color = ["grey", "pink", "blue"]
color.pop()
print(color)

#Dengan kata kunci del
barang = ["sendal", "sepatu", "sapu"]
del barang[0]
print(barang)

#Bersihkan List
barang = ["sendal", "sepatu", "sapu"]
barang.clear()
print(barang)

#Loop List
warna = ["biru", "green", "purple"]
for x in warna:
  print(x)

#Perulangan melalui nomor indeks
barang = ["sendal", "sepatu", "sapu"]
for i in range(len(barang)):
  print(barang[i])

#Menggunakan Loop While
barang = ["sendal", "sepatu", "sapu"]
i = 0
while i < len(barang):
  print(barang[i])
  i = i + 1

#Perulangan Menggunakan List Comprehension
barang = ["sendal", "sepatu", "sapu"]
[print(x) for x in barang]

buah = ["mangga", "apel", "kiwi", "jeruk", "anggur"]
newlist = []

#List comprehension
for x in buah:
  if "a" in x:
    newlist.append(x)

print(newlist)

#List comprehension satu baris
buah = ["mangga", "apel", "kiwi", "jeruk", "anggur"]
newlist = [x for x in buah if "a" in x]

print(newlist)

#Kondisi
warna = ["merah", "biru", "pink", "kuning", "hijau"]
newlist = [x for x in warna if x != "hijau"]

print(newlist)

#Kondisi tanpa If
warna = ["merah", "biru", "pink", "kuning", "hijau"]
newlist = [x for x in warna]

print(newlist)

#Dapat diulang
newlist = [x for x in range(10)]

print(newlist)

#Ekspresi
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

#Ekspresi berisi Kondisi
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

#Short List Secara Alfanumerik
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()

print(thislist)

#Short List Secara Numerik
thislist = [100, 50, 65, 82, 23]
thislist.sort()

print(thislist)

#Urutkan menurun String
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)

print(thislist)

#Urutkan menurun Angka
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)

print(thislist)

#Sesuaikan Fungsi Pengurutan
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)

print(thislist)

#Urutan Terbalik
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()

print(thislist)

#Salinan List Metode Copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()

print(mylist)

#Salinan List Metode Slice
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)

print(mylist)

#Salinan List Gunakan Operator Slice
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]

print(mylist)

#Gabungkan Dua List
#Dengan Operator + 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)

#Dengan apppend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#Dengan extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
