print(1<2)
print(1==2)
a=input()
b=input()
if(a<b):
    print("yes")
else:
    print("no")
print(bool("hello"))
#any string is true except empty string
#any number is true except 0
#any list , tuple ,set are true except empty one
print(bool())
print(bool(0))
print(bool({}))
print(bool([]))
print(bool(""))
#function can return a boolean
def abc():
    return True
if(abc()):
    print("yes")
else:
    print("no")
x = 2.5
print(isinstance(x, float))