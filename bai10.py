x=["aaa","bbb","ccc","ddd","eee"]
print(x)
print(len(x)) #kiem tra xem list co bao nhieu item
print(type(x))
#access items
print(x[1])
print(x[0])
print(x[-1])
#range of indexes
print(x[:3])
print(x[3:5])
#check list
if "aaa" in x :
    print("yes")
if "Aaaa" not in x :
    print("no")
#chang a range of item values
x[1:3] = ["yes","no"]
print(x)
x[1:3] = ["huy"]
print(x)
#insert item
x.insert(4,"huyyyyy")
print(x)
#adđ item to the end of list    
x.append("messi")
print(x)
#remove item 
x.remove("aaa")
print(x)
#remove entire list
#del x
#loop
for a in x:
    print(a, end = " ")
print()
#count
for i in range(len(x)):
    print(i, end=" ")
print()
newlist= [u for u in x if "h" in u]
print(newlist)
#sapxep alphabet
x.sort()
print(x)
x1=[4,5,6,3,6,7,8,35,66]
x1.sort()
print(x1)