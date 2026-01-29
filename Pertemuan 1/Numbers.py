#Python Numbers//Angka Python
a = 15   # int
b = 27.6 # float
c = 7j   # complex

print(type(a))
print(type(b))
print(type(c))

#Int/Bilangan Bulat
h = 100
i = 38711
j = -13280604

print(type(h))
print(type(i))
print(type(j))

#Float/Bilangan Desimal
o = 15.4
p = 28,0
q = -13.5

print(type(o))
print(type(p))
print(type(q))

r = 13e3
s = 18.6e4
t = -24.7e5

print(type(r))
print(type(s))
print(type(t))

#Complex/Bilangan Kompleks
l = 3+5j
m = 5j
n = -5j

print(type(l))
print(type(m))
print(type(n))

#Type Conversion/Konversi Tipe
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float/
e = float(x)

#convert from float to int:
f = int(y)

#convert from int to complex:
g = complex(x)

print(e)
print(f)
print(g)

print(type(e))
print(type(f))
print(type(g))

#Random Number/Angka Acak
import random

print(random.randrange(1, 10))