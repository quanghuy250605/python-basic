class huy:
    x=5
a=huy()
print(a.x)
#init
class vidu():
    def __init__(self,tham_so):
        self.t= tham_so
i=vidu(10)
print(i.t)
class vd2():
    def __init__(self,age,name):
        self.a=age
        self.n=name
    def __str__(self):
        return f"{self.a}({self.n})"
i1=vd2("19","huy")
print(i1.n)
print(i1.a)
print(i1)

        

