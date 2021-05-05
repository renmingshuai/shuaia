import  random
#1.加入字典   100个
users={}

#2.银行名称写死
bank_name="中国工商银行的昌平支行"
def welcome():
    print("**********************************************")
    print("*                                            *")
    print("*                                            *")
    print("*             中国工商银行                     *")
    print("*             账户管理系统                     *")
    print("*             v1.0                           *")
    print("*                                            *")
    print("*1.开户                                       *")
    print("*2.存钱                                       *")
    print("*3.取钱                                       *")
    print("*4.转账                                       *")
    print("*5.查询                                       *")
    print("*6.Bye！                                     *")
    print("**********************************************")
    #银行开户
def  bank_addUser(account,name,password,country,province,street,door):
    if len(users)>=100:
        return  3
    if account in users:
        return 2
    #正常开户
    users[account]={
    "name":name,
    "password":password,
    "country":country,
    "province":province,
    "street":street,
    "door":door,
    "money":0,
    "bank_name":bank_name
    }
    return 1
    #用户开户
def addUser():
    #随机8位
    li=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k",
        "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    account=""
    for i  in  range(8):
       index= random.randint(0,len(li)-1)
       account=account+li[index]
    print("用户的账号",account)
    name=input("\t请输入用户姓名")
    password= input("\t请输入用户密码")
    country = input("\t请输入您的国家：")
    province = input("\t请输入您的省份：")
    street = input("\t请输入您的街道：")
    door = input("\t请输入您的门牌号：")
    status=bank_addUser(account, name, password, country, province, street, door)
    if status==1:
        print("恭喜开户成功！")
        info = '''
         ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            国家：%s,
            省份：%s,
            街道：%s,
            门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account, name, password, country, province, street, door, users[account]["money"], bank_name))
    elif status==2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status==3:
        print("用户库已经满了,请去其他银行开户")
    # 余额不允许第一次输入，需要存钱



#银行存钱
def  bank_save():
    account=input("请输入您的用户账号")
    money1 = input("请输入你要存取的金额")
    if account in users:
        if money1.isdigit():
            money1 = int(money1)
            users[account]["money"]=money1+users[account]["money"]
            print("存钱成功")
        else:
            print("请输入你要存取的金额，别瞎弄")
    else:
        print("没有该用户，返回False")
        return  False


#查询用户
def   selectuser():
    account= input("请输入您的用户账号")
    password= input("请输入您的密码")
    if account in users:
        if password==users[account]["password"]:
            print("恭喜开户成功！")
            info = '''
                    ------------个人信息----------------
                       账号：%s,
                       用户名：%s,
                       取款密码：%s,
                       国家：%s,
                       省份：%s,
                       街道：%s,
                       门牌号：%s,
                       余额：%s,
                       开户行：%s
                       -----------------------------------
                   '''
            print(info % (account, users[account]["name"], password, users[account]["country"], users[account]["province"], users[account]["street"],users[account]["door"], users[account]["money"], bank_name))
        else:
            print("密码错误请重新输入密码")

    else:

        print("用户不存在，请添加用户")
#取钱
def   with_money():
    account= input("请输入您的用户账号")
    password = input("请输入您的密码")
    money=input("请输入您要取走的钱")
    if account in users:
        if password == users[account]["password"]:
            if money.isdigit():
                money=int(money)
                #print("money",money)
                #print(users[account]["money"],"是金额")
                if users[account]["money"]>=money:
                    users[account]["money"] = users[account]["money"]-money
                    print("取了",money,"元")
                else:
                    print("金额不足请充值")
                    return 3

            else:
                print("您的余额是数字")
        else:
            print("您的密码不对返回2")
            return 2

    else:
        print("您的用户不存在，请您添加返回1")
        return 1


#转账
def  transfer_accounts():
    name= input("请输入您转出的用户账号")
    name2 = input("请输入您转入的用户账号")
    password = input("请输入转出账号的密码")
    money = input("请输入您要转出的钱")
    if name and name2  in users:
        if password == users[name]["password"]:
            if money.isdigit():
                money = int(money)
                # print("money",money)
                # print(users[account]["money"],"是金额")
                if users[name]["money"] >= money:
                    users[name]["money"] = users[name]["money"]-money
                    users[name2]["money"] = users[name2]["money"] +money
                    print("转账成功")
                else:
                    print("金额不足请充值")
                    return 3

            else:
                print("您的余额是数字")
        else:
            print("您的密码不对返回2")
            return 2

    else:
        print("您的用户不存在，请您添加返回1")
        return 1


while True:
    welcome()
    num=input("请输入你要选择的编号")
    if num.isdigit():
        num=int(num)
        if num ==1:
            addUser()

            pass
        elif num==2:
            num=int(num)
            if num==2:
                bank_save()
                pass

        elif num==3:
            num = int(num)
            if num == 3:
                with_money()
                pass
        elif  num==4:
            num = int(num)
            if num == 4:
                transfer_accounts()
            pass
        elif num==5:
            num = int(num)
            if num == 5:
                selectuser()
            pass
        elif num==6:
            print("再见，下次再来")
            break
    else:
        print("输入非法,不要瞎弄")
