my_tuple = ("apple", "banana", "cherry")
print(my_tuple)  


my_tuple = ("apple", 42, True)
print(my_tuple)  

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  

print(my_tuple[1:3])  

for item in my_tuple:
    print(item)


print(len(my_tuple))  

x = ("apple", "banana", "cherry")
y = list(x)  
y[1] = "orange"
x = tuple(y)  
print(x)  


tuple1 = (1, 2, 3)
tuple2 = (4, 5)
result = tuple1 + tuple2
print(result)  




