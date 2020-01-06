# def demo(num,**kwargs):
#
#     print(num)
#     print(kwargs)
#     return demo1(num,**kwargs)
#
#
# def demo1(url,data=None,hd=None):
#     print(url)
#     print(data)
#     print(hd)
#
# demo(1,data="hyq",hd=12)



# def dem(**kwargs):
#     return demo(**kwargs)
# def demo(name,age):
#     print(name)
#     print(age)
# dem(name="hyq",age=12)


a = [{"1":2,"2":3},{"q":"q","w":"e"}]
for line in a:
    print(line)
    for i in line.values():
        print(i)
    if 2 in dict(line).values():
        pass

