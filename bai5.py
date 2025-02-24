a= 1
b= 1.1
c=1j
print(type(a))
print(type(b))
print(type(c))

#so nguyen integer
x1 = 1
x2 = 11111111111
x3 = -111111111
print(type(x1), type(x2), type(x3) )

#so thuc float
i1 = 1.2
i2 = -1.2
i3 = -1.34455688098766
i4 = -10e3
print(type(i1), type(i2), type(i3), type(i4))

#so phuc complex
c1 = 2j
c2 = -3j
c3 = -3 + 4j
print(type(c1), type(c2), type(c3))

#chuyen doi kieu du lieu- type conversion
a = 1
b = 1.1
c = 1+2j #complex 0 chuyen duoc sang int hoac float

A = complex(a)
B = int(b)
C = float(b)
print(type(A), type(B), type(C))

#random
import random
print(random.randrange(1,100))