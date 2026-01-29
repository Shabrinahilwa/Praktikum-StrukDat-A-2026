#Strings
print("Hai bro!")
print('Hai bro!')

#Quotes Inside Quotes/Kutip di dalam Kutip
print("It's alright")
print("She is called 'Sarah'")
print('She is called "Sarah"')

#Assign String to a Variable/Menetapkan String ke Variabel
b= "Pagi!"
print(b)

#Multiline Strings/Multi baris String
c = """Halo teman-teman,
 nama saya Shabrin.
Saya sedang belajar Python. """
print(c)

d = '''Halo teman-teman,
 nama saya Shabrin.
Saya sedang belajar Python.'''
print(d)

#Strings are Arrays/String adalah Array
e = "Siang!"
print(e[1])

#Looping Through a String/Looping Melalui String
for x in "Kucing":
  print(x)  

#String Length/Panjang String
h = "Siang!"
print(len(h))

#Check String/Memeriksa String
txt = "Jakarta adalah ibu kota Indonesia."
print("Jakarta" in txt)    

txt = "Malam hari adalah waktu yang tenang."
if "waktu" in txt:
  print("Ya, 'waktu' ada di dalam txt.")

#Check if NOT/Memeriksa jika TIDAK
txt = "Kopi latte enak sekali."
print("pahit" not in txt)

txt = "Kopi latte enak sekali"
if "pahit" not in txt:
  print("tidak, 'pahit' tidak ada di dalam txt.")

#String Slicing/Memotong String

#Slicing/Mengiris
k = "Halo, gurl!"
print(k[2:5])

#Slice From the Start/Memotong dari start
m = "Halo, gurl!"
print(m[:5])

#Slice To the End/Memotong sampai akhir
n = "Halo, gurl!"
print(n[2:])

#Negative Indexing/Pengindeksan Negatif
o = "Halo, gurl!"
print(o[-5:-2])

#Modify Strings/Memodifikasi String

#Upper Case/Huruf Besar
p = "Halo, gurl!"
print(p.upper())

#Lower Case/Huruf Kecil
q = "Halo, gurl!"
print(q.lower())

#Remove Whitespace/Menghapus Spasi
r = " Halo, gurl! "
print(r.strip()) # returns "Hello, World!"

#Replace String/Mengganti String
s = "Halo, gurl!"
print(s.replace("H", "J"))

#Split String/Memisah String
t = "Halo, gurl!"
print(t.split(",")) # returns ['Hello', ' World!']

#String Concatenation/Penggabungan String
u = "Halo"
v= "Gurl"
w = u + v
print(w)

x = "Halo"
y = "Gurl"
z = x + " " + y
print(z)

#F-Strings
Umur = 19
txt = f"Nama saya Shabrin, umur saya {Umur}"
print(txt)

#Placeholders and Modifiers/Pengisi dan Modifikator
Harga = 90
txt = f"Harganya {Harga} ribu"
print(txt)

Harga = 80
txt = f"Harganya {Harga:.2f} ribu"
print(txt)

txt = f"Harganya {59 * 5} ribu"
print(txt)

#Escape Character/Karakter Escape
txt = "Film kesukaannya adalah \"Jumbo\" tayang pada 2024."
