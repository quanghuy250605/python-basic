mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  
print(next(myit))  
print(next(myit))  

#iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))  
print(next(myiter))  
print(next(myiter))  
#StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
for x in myclass:
    print(x) 


