
import random
from DBUtils import  update
from  DBUtils import  select

#银行库

bank_name = "中国工商银行昌平支行"

def welcome():
    print("---------------------------------")
    print("-     中国工商银行账户管理系统V1.0     -")
    print("---------------------------------")
    print("-   1.开户                       -")
    print("-   2.存钱                       -")
    print("-   3.取钱                       -")
    print("-   4.转账                       -")
    print("-   5.查询                       -")
    print("-   6.Bye!                       -")
    print("----------------------------------")

# 银行的开户逻辑
def bank_addUser(account,username,password,country,province,street,door):
    # 判断是否已满
    sql="select count(*) from bank"
    date=select(sql,[])
    if date[0][0]>=100:
        return 3
    # 判断是否存在
    sql1="select * from bank where username=%s"
    user=select(sql1,account)
    if len(user) !=0:
        return 2
    #正常开户
    sql2="insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    parm=[account,username,password,country,province,street,door,0.0,bank_name]
    update(sql2,parm)
    return 1
# 银行的存钱方法
def bank_saveMoney(ac,money):
    sql1 = "select * from bank where username=%s"
    user = select(sql1, ac)
    print(len(user))
    if len(user) != 0:
        sql="update bank  set money=money+%s where username=%s"
        parm=[money,ac]
        update(sql,parm)
        print("存钱成功")
    else:
        print("没有该用户")
        return  False;
    #取钱
def bank_takeMoney(account,password,money):
    sql1 = "select * from bank where username=%s"
    user = select(sql1, account)

    if len(user) != 0:
        sql2 = "select password from bank where username=%s"
        password1= select(sql2, account)
        if password1[0][0]==password:
            sql3="select money from  bank where username=%s"
            money1=select(sql3,account)
            if money1[0][0]>=money:
                sql4="update bank set money=money-%s where username =%s"
                parm=[money,account]
                update(sql4,parm)
                print("取了",money,"元")
            else:
                print("取钱失败请充钱")
                return 3

        else:
            print("密码错误")
            return 1
    else:
        print("用户名不存在")
        return 2
#转账
def bank_outmoney(account,account1,password,money):
    sql1 = "select * from bank where username=%s"
    user = select(sql1, account)
    sql1 = "select * from bank where username=%s"
    user1 = select(sql1, account1)
    if len(user) != 0 and len(user1)!=0:
        sql2 = "select password from bank where username=%s"
        password1 = select(sql2, account)
        if password1[0][0] == password:
            sql3 = "select money from  bank where username=%s"
            money1 = select(sql3, account)
            if money1[0][0]-money>=0:
                sql4="update bank set money=money-%s where username=%s"
                parm=[money,account]
                select(sql4,parm)
                sql5="update bank set money=money+%s where username=%s"
                parm1=[money,account1]
                select(sql5,parm1)
                print("转账成功")
            else:
                print("转账失败，请充钱")
                return 3
        else:
            print("密码错误")
            return 2

    else:
        print("没有该用户")
        return 1

#查询
def  chaxun(account,password):
    sql1 = "select * from bank where username=%s"
    user = select(sql1, account)

    if len(user) != 0:
        sql2 = "select password from bank where username=%s"
        password1 = select(sql2, account)

        if password1[0][0] == password:
            sql3 = "select * from bank where username=%s"
            user2=select(sql3,account)
            print(user2)
            username = user2[0][1]
            country = user2[0][3]
            province = user2[0][4]
            street = user2[0][5]
            door = user2[0][6]
            money = user2[0][7]
            bank_name = user2[0][8]

            info = '''
                        ------------个人信息----------------
                        账号：%s,
                        用户名：%s,
                        取款密码：%s,
                        地址信息：
                            国家：%s,
                            省份：%s,
                            街道：%s,
                            门牌号：%s,
                        余额：%s,
                        开户行：%s
                        -----------------------------------
                    '''
            print(info %(account,username,password,country,province,street,door,money,bank_name))


        else:
            print("密码错误")
    else:
        print("用户不存在")



# 用户开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    name = input("请输入用户名：")
    password = input("请输入您的密码（6位数字）：")
    print("接下来要输入您的地址信息：")
    country = input("\t输入国家：")
    province = input("\t输入省份：")
    street =  input("\t输入街道：")
    door = input("\t输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    status = bank_addUser(account,name,password,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！")
        info = '''
            ------------个人信息----------------
            账号：%s,
            用户名：%s,
            取款密码：%s,
            地址信息：
                国家：%s,
                省份：%s,
                街道：%s,
                门牌号：%s,
            余额：%s,
            开户行：%s
            -----------------------------------
        '''
        print(info % (account,name,password,country,province,street,door,0,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")
    elif status == 3:
        print("对不起，该银行库已满，请携带证件到其他银行办理！！！")

def saveMoney():
    account = input("请输入账号")
    m = input("存入的金额")
    m=float(m)
    bank_saveMoney(account,m)
def takeMoney():
    print(11111111111111111111111)
    account = input("请输入账号")
    password=input("请输入密码")
    money = input("取出的金额")
    money = float(money)
    bank_takeMoney(account,password,money)
def out_money():
    account = input("请输入转出的账号")
    account1 = input("请输入转入的账号")
    password = input("请输入转出账号的密码")
    money = input("转出的金额")
    money = float(money)
    bank_outmoney(account,account1,password,money)

def selectcha():
    account = input("请输入账号")
    password = input("请输入账号的密码")
    chaxun(account,password)







# 开户方法
def addUser():
    # 随机获取账号
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","e","f"]
    account = ""
    for i in range(8):
        index = random.randint(0, len(li) - 1)
        account = account + li[index]
    username = input("请输入用户名")
    password = input("请输入密码")
    country = input("居住地址：1.国家：")
    province =  input("省份")
    street = input("街道")
    door = input("门牌号")
    # 调用银行的开户方法完成开户操作  返回 1 2 3
    status = bank_addUser(account,username,password,country,province,street,door)
    # 判断1   2   3
    if status == 1:
        print("恭喜开户成功！")
        info = '''
                  ------------个人信息----------------
                  账号：%s,
                  用户名：%s,
                  取款密码：%s,
                  地址信息：
                      国家：%s,
                      省份：%s,
                      街道：%s,
                      门牌号：%s,
                  余额：%s,
                  开户行：%s
                  -----------------------------------
              '''
        print(info % (account, username, password, country, province, street, door, 0, bank_name))
    elif status == 2:
        print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")


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
                saveMoney()
                pass

        elif num==3:
            num = int(num)
            if num == 3:
                takeMoney()
                pass
        elif  num==4:
            num = int(num)
            if num == 4:
                out_money()
                pass
        elif num==5:
            num = int(num)
            if num == 5:
                selectcha()
                pass
        elif num==6:
            print("再见，下次再来")
            break
    else:
        print("输入非法,不要瞎弄")