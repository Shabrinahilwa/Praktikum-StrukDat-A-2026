#Dapatkan Nilai Properti Private dengan Method Getter
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur  # Properti privat

  def get_umur(self):
    return self.__umur

orang1 = Orang("Ryul", 20)
print(orang1.get_umur())

#Ubah Nilai Properti Private dengan Method Setter
class Orang:
  def __init__(self, nama, umur):
    self.nama = nama
    self.__umur = umur  # Properti privat

  def get_umur(self):
    return self.__umur

  def set_umur(self, umur):
    if umur > 0:
      self.__umur = umur
    else:
      print("Umur harus bernilai positif")

orang1 = Orang("Woojin", 20)
print(orang1.get_umur())

orang1.set_umur(18)
print(orang1.get_umur())

#Properti Protected
class Orang:
  def __init__(self, nama, gaji):
    self.nama = nama
    self._gaji = gaji  # Properti protected
orang1 = Orang("Linus", 50000)
print(orang1.nama)
print(orang1._gaji)  # Bisa diakses, tetapi tidak disarankan