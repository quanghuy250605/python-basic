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