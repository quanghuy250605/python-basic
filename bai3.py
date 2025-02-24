a=10
b=20
print (a+b)
d=2+3j
c="huy"
print(c)
print(type(c))
print(type(a))
print(c.upper())
print(c[2])
print(d.imag)
print(d.real)

#variable name-tên biến
#start with letter or underscore character
#cant start with number
#use a-z, 0-9, "_"
#case sensitive 
#cant be any python keyword(def , print,if ,else.....)

#allow assign values to multiple variables
x, y, z= "1", "2", "3"
print(x,y,z)
# the number of variables = the number of values

#can assign 1 values to multiple variables
x1= y1= z1= "1234556"
print(x1, y1, z1)

#unpack a collection
color = ["red", "blue", "orange"]
x4, x5, x6 = color
print(x4, x5, x6, sep= "\n")

#global variables

e ="hello world"
def abc():
    e = "commnent"
    print("this is:",e)
abc()
print("this is:",e)
#neu dat ten bien trung ten global variable thi ham se su dung bien duoc dat trong ham

#keyword global
o="huy2"
def abcd():
    global o
    o = "huy"
abcd()
print("toi ten la :",o)
