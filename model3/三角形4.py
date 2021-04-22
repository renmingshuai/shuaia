
a=input("请输入三角形一边")
a=int(a)
b=input("请输入三角形一边")
b=int(b)
c=input("请输入三角形一边")
c=int(c)
if  a==b==c:
    print("等边三角形")
elif a == b or b == c or a == c:
     print("等腰三角形")
elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
     print("构成直角三角形")
elif a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    print("构成三角形")



else:
    print("不能构成三角形")

