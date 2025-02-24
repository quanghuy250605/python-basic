# text type : str
# number type :int,float,complex(so phức)
# sequence type(xau, chuoi) :list(được thêm bớt trùng lặp), tuple(cố định), range
# mapping type :dict
# setting type :set --set><map
# boolean type :bool(true/false)
# binary types :bytes(dạng nhị phân),bytearray,memoryview
# none type :none

a = str("hello world")
print(a)
print(type(a))
b = float(5.439399393)
print(b)
print(type(b))
c = complex(2+3j)
print(c)
print(type(c))
i = list(("con cho", "con meo", "con ga"))
print(i)
print(type(i))
x=tuple(("aaa","vvv","ccc"))
print(x[1])
print(type(x)) 
for u in range(5):
    print(u, end=" ")
print()
print(type(u))
w = dict(a ="huy", b={10,22,33,44,55,66,77})
print(w["b"])  
print(type(w))
e = set(("aaa" , "aaa", "bbb", "bbb"))
print(e)
print(type(e))
q = bool(5)
print(q)
print(type(q))
t = b"abcxyz"
print(t[0])
print(type(t))
y = None
if y == None:
    print("okokokkok")
    print(type(y))
