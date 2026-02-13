#Dictionary
handphone = {
  "merek": "Samsung",
  "tipe": "S25",
  "tahun": 2024
}
print(handphone)

#Item Dictionary
handphone = {
  "merek": "Samsung",
  "tipe": "S25",
  "tahun": 2024
}
print(handphone["merek"])

#Tipe Data – Item Dictionary
handphone = {
  "merek": "Samsung",
  "tipe": "S25",
  "tahun": 2024,
  "warna": ["hitam", "putih", "silver"]
}
print(handphone)

#Konstruktor dict()
biodata = dict(nama = "Ryul", umur = 19, negara = "Korea")
print(biodata)  

#Akses Item 
handphone = {
  "merek": "Samsung",
  "tipe": "S25",
  "tahun": 2024
}
x = handphone.get("tahun")
print(x)

#Dapatkan Key
handphone = {
  "merek": "Samsung",
  "tipe": "S25",
  "tahun": 2024
}
x = handphone.keys()
print(x)

#Key Baru
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}

x = handphone.keys()

print(x) #before the change

handphone["warna"] = "hitam"

print(x) #after the change

#Dapatkan Nilai
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}

x = handphone.values()

print(x) #before the change

handphone["tahun"] = 2025

print(x) #after the change

#Periksa Apakah Key Tersebut Ada
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}
if "merek" in handphone:
  print("Iya, key ada pada dictionary")

#Perbarui Kamus
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}
handphone.update({"tipe": "A36"})
print(handphone)

#Copy Dictionary
#copy()
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}
mydict = handphone.copy()
print(mydict)

#dict()
handphone = {
"merek": "Samsung",
"tipe": "S25",
"tahun": 2024
}
mydict = dict(handphone)
print(mydict)

#Nested Dictionary
lngshot = {
  "member 1": {
    "nama": "Ohyul",
    "tahun": 2006
  },
  "member 2": {
    "nama": "Ryul",
    "tahun": 2006
  },
  "member 3": {
    "nama": "Woojin",
    "tahun": 2008
  }
}
print(lngshot)

#Buat Satu Kamus
member_1 = {
  "nama": "Ohyul",
  "tahun": 2006
}
member_2 = {
  "nama": "Ryul",
  "tahun": 2006
}
member_3 = {
  "nama": "Woojin",
  "tahun": 2008
}

lngshot = {
  "Member 1" : member_1 ,
  "Member 2" : member_2,
  "Member 3" : member_3
}
print(lngshot)

#Mengakses Item dalam Nested Loop
member_1 = {
  "nama": "Ohyul",
  "tahun": 2006
}
member_2 = {
  "nama": "Ryul",
  "tahun": 2006
}
member_3 = {
  "nama": "Woojin",
  "tahun": 2008
}

lngshot = {
  "Member 1" : member_1,
  "Member 2" : member_2,
  "Member 3" : member_3
}
print(lngshot["Member 1"]["nama"])

lngshot = {
  "Member 1": {
    "nama": "Ohyul",
    "tahun": 2006
  },
  "Member 2": {
    "nama": "Ryul",
    "tahun": 2006
  },
  "Member 3": {
    "nama": "Woojin",
    "tahun": 2008
  }
}
for x, obj in lngshot.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])
