def a(x,y):
    print(x,y)
a("quang","huy")
# con trỏ
def b(*x):
    print("my name is ", x[2])
b("huy", "quân", "hello")
#keyword
def c(x1,x2,x3):
    print("my name is", x1)
c(x1="huy",x2="quang",x3="anh")
#con trỏ **
def e(**e1):
    print("my name is", e1["e2"])
e(e2="huy", e3="quang")
def countries(country=""):
    print("im from",country)
countries("thailand")
countries("america")
#return
def math(x):
    return x+10
print(math(3))
