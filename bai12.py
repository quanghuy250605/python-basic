my_set = {"apple", "banana", "cherry"}
print(my_set)  

my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)   

my_set = {"apple", "banana"}
my_set.add("cherry")
print(my_set)  

my_set.update(["orange", "grape"])
print(my_set)  

my_set.remove("banana")  
my_set.clear()
print(my_set)

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)


set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
result = set1.union(set2)
print(result)  

set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
result = set1.intersection(set2)
print(result) 

result = set1.difference(set2)
print(result) 

result = set1.symmetric_difference(set2)
print(result) 








