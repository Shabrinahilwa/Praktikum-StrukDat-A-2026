#Boolean Values
print(100 > 99)
print(100 == 99)
print(100 < 99)

a = 93
b = 42

if b > a:
  print("b besar dari a")
else:
  print("b lebih kecil dari a")

#Evaluate Values and Variables/Evaluasi Nilai dan Variabel
print(bool("Hai!"))
print(bool(5))

x = "Hai"
y = 7

print(bool(x))
print(bool(y))

#Most Values are True/Kebanyakan Nilai True
bool("x,y,z")
bool(123)
bool(["Jeruk", "Manggis", "Durian"])

#Some Values are False/Beberapa Nilai False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#Functions can Return a Boolean/Fungsi dapat Mengembalikan Boolean
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("Iya!")
else:
  print("Tidak!")

x = 200
print(isinstance(x, int))