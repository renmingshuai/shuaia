from DBUtils import DBUtils
from welcome import Welcome
from User import User
from Address import Address
from Bank import Bank
from HelpUtils import Utils

DB = DBUtils()
welcome = Welcome()
User = User()
Address = Address()
Bank = Bank()
Utils = Utils()


# 开户方法
def addUser():
    # 随机生成账号
    account = Utils.getRandom()
    User.setUsername(Utils.inputHelp("用户名"))
    User.setPassword(Utils.inputHelp("密码"))
    Address.setCounrry(Utils.inputHelp("国家"))
    Address.setProvince(Utils.inputHelp("省份"))
    Address.setStreet(Utils.inputHelp("街道"))
    Address.setDoor(Utils.inputHelp("门牌号"))
    # username = input("请输入您的姓名：")
    # password = input("请输入您的密码（6个数字）：")
    # print("接下来请输入您的地址信息")
    # counrry = input("\t请输入您的国家：")
    # province = input("\t请输入省份：")
    # street = input("\t请输入街道：")
    # door = input("\t请输入门牌号：")
    # 余额不允许第一次输入，需要存钱

    start = Bank.bank_addUser(account,User.getUsername(),User.getPassword(),Address.getCounrry(),Address.getProvicne(),Address.getStreet(),Address.getDoor())
    if start == 1:
        print("开户成功!")

        info = '''
            ----------- 个人信息-------------
            账号： %s,
            用户名： %s,
            取款密码： %s,
            地址信息： 
                国家： %s,
                省份： %s,
                街道： %s,
                门牌号： %s,
            余额： %s,
            开户行： %s
            ---------------------------------
        '''
        print(info % (account,User.getUsername(),User.getPassword(),Address.getCounrry(),Address.getProvicne(),Address.getStreet(),Address.getDoor(),0,Bank.getBankName()))
    if start == 2:
        print("该用户名已经存在！！！")
    if start == 3:
        print("银行用户库已满！！！")

#存钱方法
def addMoney():
    User.setAccount(Utils.inputHelp("账号"))
    Bank.setMoney(Utils.inputHelp("存储金额"))


    start = Bank.bank_addMoney(User.getAccount(),Bank.getMoney())
    if start == 1:
        print("存入成功！")
    if start == False:
        print("您输入的账号不存在！")

# 取钱方法
def withdrawal():
    User.setAccount(Utils.inputHelp("账号"))
    User.setPassword(Utils.inputHelp("密码"))
    Bank.setMoney(Utils.inputHelp("要取出的金额"))


    start = Bank.bank_withdrawal(User.getAccount(),User.getPassword(),Bank.getMoney())
    if start == 0:
        print("取款成功！")
    if start == 1:
        print("账号不存在！")
    if start == 2:
        print("密码不对")
    if start == 3:
        print("账户余额不足")

# 转账方法
def transfer():
    account1 = Utils.inputHelp("转出的账号")
    account2 = Utils.inputHelp("要转入的账号")
    password = Utils.inputHelp("您转出账号的密码")
    money = Utils.inputHelp("您要转出的金额")

    start = Bank.bank_transfer(account1,account2,password,money)
    if start == 0:
        print("转账成功！")
    if start == 1:
        print("您输入的账号不正确！")
    if start == 2:
        print("您输入的密码不正确！")
    if start == 3:
        print("您的账户余额不足！")

# 查询方法
def seek():
    User.setAccount(Utils.inputHelp("您的要查询的账号"))
    User.setPassword(Utils.inputHelp("密码"))

    start = Bank.bank_seek(User.getAccount(),User.getPassword())
    if start == 0:
        # 查询表中数据
        sql = "select * from bank where username = %s and password = %s"
        param = [User.getAccount(),User.getPassword()]
        # 执行sql
        data = DB.Select(sql, param)
        for i in data:
            account = data[0][0]
            username = data[0][1]
            password = data[0][2]
            cunrry = data[0][3]
            province = data[0][4]
            street = data[0][5]
            door = data[0][6]
            money = data[0][7]
            bank_name = data[0][8]
        print("以下为您的账号信息")
        info = '''
                ----------- 个人信息-------------
                账号： %s,
                用户名： %s,
                取款密码： %s,
                地址信息： 
                        国家： %s,
                        省份： %s,
                        街道： %s,
                        门牌号： %s,
                余额： %s,
                开户行： %s
                ---------------------------------
                '''
        print(info % (account,username,password,cunrry,province,street,door,money,bank_name))
    if start == 1:
        print("该用户不存在")
    if start == 2:
        print("您输入的密码不正确")

while True:

    welcome.welcome()
    num = input("请输入您的业务编号：")
    if num.isdigit():
        num = int(num)
        if num == 1:
            # 开户
            addUser()
        elif num == 2:
            # 存款
            addMoney()
        elif num == 3:
            # 取款
            withdrawal()
        elif num == 4:
            # 转账
            transfer()
        elif num == 5:
            # 查询
            seek()
        elif num == 6:
            print("欢迎下次光临！")
            break
        else:
            print("输入非法！！！请重新输入！！！")
    else:
        print("输入非法！！！请重新输入！！！")