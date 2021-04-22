name="root"
password="admin"
count=0
while True:
    count=count+1
    name1 = input("请输入用户名")
    password1=input("请输入密码")
    if count>=3:
        print("用户名和密码被冻结")
        break
    if name1 != name and password1 != password:
            print("用户名和密码全部错误")
    elif password1!=password:
        print("密码错误")
    elif  name1!=name:
        print("用户名错误")

    else:
        print("登录成功")
        break
