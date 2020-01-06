num = 10

def demo1():
    global num
    num = 20
    print("demo1:%s"%num)

def demo2():
    print("demo2是：%s"%num)


demo1()
print(num)
demo2()

