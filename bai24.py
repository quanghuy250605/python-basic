def func():
    x = 300  
    print(x)

func()

def func1():
    x = 300
    def func2():
        print(x)  # ✅ Có thể truy cập x từ hàm cha
        func2()

func()

