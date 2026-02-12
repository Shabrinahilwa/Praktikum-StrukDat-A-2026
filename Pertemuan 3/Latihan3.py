class Person:
    def __init__(self, nama, jenis_kelamin, umur,):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin
        self.umur = umur

class Karyawan(Person):
    def __init__(self, nama, jenis_kelamin, umur, gaji):
        super().__init__(nama, jenis_kelamin, umur)
        self.__gaji = gaji #protected
    
    def get_gaji(self):
        return self.__gaji
    
class Rekening:
    def __init__(self, no_Rek,PIN):
        self.no_rek = no_Rek
        self.__PIN = PIN
    
    def get_PIN(self):
        return self.__PIN
    
    def set_PIN(self, pinBaru):
        self.__PIN = pinBaru

p1 = Karyawan ("Shabrin", "Perempuan", 19, 3000000)
r1 = Rekening("345", "2828")

print(r1.get_PIN())
print(p1.nama)
print(p1.get_gaji())

