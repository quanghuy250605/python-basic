my_dict = {
    "name": "huy",
    "age": 30,
    "city": "vietnam"
}
print(my_dict)  

print(my_dict["name"])  

print(my_dict.get("age"))  # 30
print(my_dict.get("job", "Not found"))

my_dict["job"] = "Developer" 
my_dict["age"] = 31

del my_dict["city"]
print(my_dict)  
my_dict.clear()
print(my_dict)  




