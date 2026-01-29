#Creating Variables
ab = 5
ac = "Ryul"
print(ab)
print(ac)

ad = 4       # ad is of type int
ae = "Ryul" # ae is now of type str
print(ad)

#Casting
af = str(7)    # af will be '7'
ag = int(7)    # ag will be 7
ah = float(7)  # ah will be 7.0

#Get the Type
ai = 5
aj = "Ryul"
print(type(ai))
print(type(aj))

#Single or Double Quotes?
ak = "Ryul"
# is the same as
al = 'Ryul'

#Case-Sensitive
am = 4
AN = "Ryul"
#AN will not overwrite am

#Variable Names
myvar = "Ryul"
my_var = "Ryul"
_my_var = "Ryul"
myVar = "Ryul"
MYVAR = "Ryul"
myvar2 = "Ryul"

#Multi Words Variable Names
#Camel Case
MyVariableName = "Ryul"

#Pascal Case
VariableName = "Ryul"

#Snake Case
variable_name = "Ryul"

#Assign Multiple Values

#Many Values to Multiple Variables
a = b = c = "Semangka"
print(a)
print(b)
print(c)

#One Value to Multiple Variables
d = e = f = "Nanas"
print(d)
print(e)
print(f)

#Unpack a Collection
fruits = ["Apel", "Pisang", "Jeruk"]  
g, h, i = fruits
print(g)
print(h)
print(i)

#Output Variables
j = "Cool"
print(j)

k = "Python"
l = "is"
m = "cool"
print(k, l, m)

n = "Python "
o = "is "
p = "cool"
print(n + o + p)

q = 5
r = 10
print(q + r)

s = 10
t = "Ryul"
print(s, t)

#Global Variables
u = "Cool"

def myfunc():
  print("Python is " + u)

myfunc()

v = "Cool"

def myfunc():
  v = "great"
  print("Python is " + v)

myfunc()

print("Python is " + v)

#The global Keyword
def myfunc():
  global z
  z = "Great"   

myfunc()

print("Python is " + z)

x = "Cool"

def myfunc():
  global x
  x = "Great"

myfunc()

print("Python is " + x)