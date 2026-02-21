class Mobil:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def bergerak(self):
    print("Mengemudi!")

class Perahu:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def bergerak(self):
    print("Berlayar!")

class Pesawat:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model

  def bergerak(self):
    print("Terbang!")

mobil1 = Mobil("Audi", "A4")        # Membuat objek Mobil
perahu1 = Perahu("Ibiza", "Touring 20")  # Membuat objek Perahu
pesawat1 = Pesawat("Lion Air", "747")      # Membuat objek Pesawat

for kendaraan in (mobil1, perahu1, pesawat1):
  kendaraan.bergerak()
  