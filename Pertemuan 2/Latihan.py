#Nomor 1
nilai=[75, 80, 65, 90, 85]
nilai.append(95)
print(nilai)

nilai = [75, 80, 65,90,85]
nilai.remove(65)
print(nilai)

nilai = [75, 80, 65, 90, 85]
nilai.sort()
print(nilai)

nilai = [65, 75, 80, 85, 90]
print(nilai[len(nilai)-1])

nilai = [65, 75, 80, 85, 90]
print(nilai[0])

nilai = [65, 75, 80, 85, 90]
print(len(nilai))

nilai= [65, 75, 80, 85, 90]
rata_rata = sum(nilai) / len(nilai)
print(rata_rata)

#Nomor 2
dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print (dosen[1])

dosen = ("D001", "Dr. Andi", "Struktur Data", 12)
print (dosen[2])

dosen = ("D001", "Dr. Andi", "Struktur Data", 14)
print (dosen)
#variabel dosen tetap bisa di print 

#tuple tidak dapat berubah-ubah

#Nomor 3
keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
keahlian_C = keahlian_A.union(keahlian_B)
print(keahlian_C)

keahlian_A = {"Python", "Java", "SQL", "Git"}
keahlian_B = {"Python", "C++", "Git", "Docker"}
print (keahlian_A.difference(keahlian_B))





