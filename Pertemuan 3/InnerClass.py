#Inner Class (Kelas Dalam)
class Luar:
  def __init__(self):
    self.nama = "Outer Class"

  class Dalam:
    def __init__(self):
      self.nama = "Inner Class"

    def tampilkan(self):
      print("Ini adalah Inner Class")

luar = Luar()
print(luar.nama)

#Mengkases Inner Class dari Luar Class
class Luar:
  def __init__(self):
    self.nama = "Outer"

  class Dalam:
    def __init__(self):
      self.nama = "Inner"

    def tampilkan(self):
      print("Halo dari Inner Class")

luar = Luar()
dalam = luar.Dalam()
dalam.tampilkan()

#Mengakses Kelas Luar dari Kelas Dalam
class Outer:
  def __init__(self):
    self.name = "Ohyul"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Nama Outer Class: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()

#Contoh Praktis Inner Class
class Mobil:
  def __init__(self, merek, model):
    self.merek = merek
    self.model = model
    self.mesin = self.Mesin()

  class Mesin:
    def __init__(self):
      self.status = "Mati"

    def nyalakan(self):
      self.status = "Menyala"
      print("Mesin dinyalakan")

    def matikan(self):
      self.status = "Mati"
      print("Mesin dimatikan")

  def jalan(self):
    if self.mesin.status == "Menyala":
      print(f"Mengemudi {self.merek} {self.model}")
    else:
      print("Nyalakan mesin terlebih dahulu!")

mobil = Mobil("Toyota", "Corolla")
mobil.jalan()
mobil.mesin.nyalakan()
mobil.jalan()

#Beberapa Inner Class
class Komputer:
  def __init__(self):
    self.prosesor = self.Prosesor()
    self.memori = self.Memori()

  class Prosesor:
    def proses(self):
      print("Memproses data...")

  class Memori:
    def simpan(self):
      print("Menyimpan data...")

komputer = Komputer()
komputer.prosesor.proses()
komputer.memori.simpan()