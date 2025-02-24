print("hello world") 
print('hello world')
a= "hello world"
print(a)
b='hello world'
print(b)
#co the xuong dong khi dung """...."""
c= """1+1=2,
2+2=4,
3+3=6"""
print(c)
#strings are arrays
x = "hello world"
print(x[6])
#looping through string (vong lap)
for a1 in "hello world":
    print(a1, end = " ")
print()
#string length
a2 = "hello world"
print(len(a2))
#check strings
a3 = "my name is huy"
if "my" in a3 :
    print("yes, 'my' is present")
#silce
a4 =" manchester is red "
print(a4[2:4])#khong lay vi tri thu 4
print(a4[-4:-2])
#upper case (in hoa)
print(a4.upper())
#lower case (in thuong)
print(a4.lower())
#remove whitespace (bo khoang trang)
print(a4.strip())
#replace strings
print(a4.replace("red", "blue"))
#split strings
print(a4.split())
#string concatenation
a5 = "sunday is"
a6 = "the king play"
a7 = a5+" " +a6
print(a7)
#f-string
a8 = 19
a9 = f"i am {a8} years old"
print(a9)
x1 = f"i am {10+9} years old"
print(x1)
x2 = 2.3490
x3 = f"its price is {x2:.2f} dollars"
print(x3)
#escape character
print("cr7 is a \"GOAT\"")