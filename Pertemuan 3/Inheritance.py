#Buat Parent Class
class Orang:
  def __init__(self, nama_depan, nama_belakang):
    self.firstname = nama_depan
    self.lastname = nama_belakang

  def printnama(self):
    print(self.firstname, self.lastname)

x = Orang("Kim", "Ryul")
x.printnama()

#Buat Child Class
class Orang:
  def __init__(self, nama_depan, nama_belakang):
    self.firstname = nama_depan
    self.lastname = nama_belakang

  def printnama(self):
    print(self.firstname, self.lastname)

class Siswa(Orang):
  pass

x = Siswa("Kwon", "Ohyul")
x.printnama()

#Buat Child Class dengan fungsi __init_()
class Orang:
  def __init__(self, nama_depan, nama_belakang):
    self.firstname = nama_depan
    self.lastname = nama_belakang

  def printname(self):
    print(self.firstname, self.lastname)

class Siswa(Orang):
  def __init__(self, nama_depan, nama_belakang):
    Orang.__init__(self, nama_depan, nama_belakang)


x = Siswa("Eom", "Sean")
x.printname()

#Gunakan fungsi super()
class Orang:
  def __init__(self, nama_depan, nama_belakang):
    self.firstname = nama_depan
    self.lastname = nama_belakang

  def printname(self):
    print(self.firstname, self.lastname)

class Siswa(Orang):
  def __init__(self, nama_depan, nama_belakang):
    super().__init__(nama_depan, nama_belakang)
    self.tahunKelulusan = 2025
    
x = Siswa("Mike", "Olsen")
print(x.tahunKelulusan)

#Tambahkan Metode
def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

def printname(self):
    print(self.firstname, self.lastname)

class Siswa(Orang):
  def __init__(self, nama_depan, nama_belakang, tahun):
    super().__init__(nama_depan, nama_belakang)
    self.tahunkelulusan = tahun

  def Ucapan(self):
    print("Selamat datang", self.firstname, self.lastname,
           "di angkatan Tahun", self.tahunkelulusan)

x = Siswa("Jung", "Woojin", 2027)
x.Ucapan()

