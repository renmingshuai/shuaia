a=input("请输入三角形一边")
a=int(a)
b=input("请输入三角形一边")
b=int(b)
c=input("请输入三角形一边")
c=int(c)
a>0
b>0
c>0

if  a+b>c and a+c>b and b+c>a:
    print("构成三角形")
    if  a==b==c:
        print("等边三角形")
    if a == b!=c or b == c!=a or a == c!=b:
        print("等腰三角形")
    if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
        print("构成直角三角形")
else:
    print("不能构成三角形")

