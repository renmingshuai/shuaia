import random
from DBUtils import DBUtils

DB = DBUtils()

class Bank():
    __money = 0
    __bank_name = "中国工商银行的昌平支行"

    def setMoney(self,money):
        self.__money = money
    def getMoney(self):
        return self.__money

    def getBankName(self):
        return self.__bank_name


    # 开户逻辑
    def bank_addUser(self,account, username, password, counrry, province, street, door):
        # 判断是否已满
        sql = "select count(*) from bank"
        data = DB.Select(sql, [])
        if data[0][0] >= 100:
            return 3

        # 判断是否存在
        sql1 = "select count(*) from bank where username = %s"
        data2 = DB.Select(sql1, account)
        if data2[0][0] != 0: #(())
            return 2

        # 正常开户
        # 插入数据
        sql2 = "insert into bank values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account, username, password, counrry, province, street, door, 0, self.__bank_name]
        # 执行sql
        DB.Update(sql2, param2)
        return 1

    # 存钱逻辑
    def bank_addMoney(self,account, money):
        # 查询表中数据
        sql = "select username from bank where bank.username = %s"
        param = [account]
        # 执行sql
        data = DB.Select(sql, param)
        # 获取是否存在输入的account
        num = len(data)

        if num == 1:
            # 修改表中数据
            sql = "update bank set money = money + %s where username = %s"
            param = [money, account]
            DB.Update(sql, param)
            return 1
        if num == 0:
            return False
    # 取钱逻辑
    def bank_withdrawal(self,account, password, getmoney):
        # 查询表中数据
        sql = "select count(username) from bank where bank.username = %s"
        data = DB.Select(sql, account)
        # 获取是否存在输入的account

        if data[0][0] == 1:
            sql = "select count(*) from bank where bank.username = %s and bank.password = %s"
            param = [account, password]
            data = DB.Select(sql, param)
            if data[0][0] == 1:
                sql = "select count(*) from bank where bank.username = %s and bank.password = %s and money >= %s"
                param = [account, password, getmoney]
                data = DB.Select(sql, param)
                if data[0][0] == 1:
                    sql = "update bank set bank.money =bank.money - %s where bank.money >= %s"
                    param = [getmoney, getmoney]
                    DB.Update(sql, param)
                    return 0
                if data[0][0] == 0:
                    return 3
            if [0][0] == 0:
                return 2
        else:
            return 1
    # 转账逻辑
    def bank_transfer(self,account1, account2, password, money):
        # 查询表中数据
        sql = "select count(*) from bank where bank.username = %s or bank.username = %s"
        param = [account1, account2]
        # 执行sql
        data = DB.Select(sql, param)

        if data[0][0] == 2:
            sql = "select count(*) from bank where bank.username = %s and bank.password = %s"
            param = [account1, password]
            data = DB.Select(sql, param)
            if data[0][0] == 1:
                sql = "select count(*) from bank where bank.username = %s and bank.money >= %s"
                param = [account1, money]
                data = DB.Select(sql, param)
                if data[0][0] == 1:
                    sql = "update bank set bank.money = bank.money - %s where bank.username = %s"
                    param = [money, account1]
                    DB.Update(sql, param)
                    sql1 = "update bank set bank.money = bank.money + %s where bank.username = %s"
                    param1 = [money, account2]
                    DB.Update(sql1, param1)
                    return 0
                if data[0][0] == 0:
                    return 3
            if data[0][0] == 0:
                return 2
        else:
            return 1
    # 查询逻辑
    def bank_seek(self,account, password):
        # 查询表中数据
        sql = "select count(*) from bank where username = %s"
        param = [account]
        # 执行sql
        data = DB.Select(sql, param)
        if data[0][0] == 1:
            sql = "select count(*) from bank where username = %s and password = %s"
            param = [account, password]
            data = DB.Select(sql, param)
            if data[0][0] == 1:
                return 0
            if data[0][0] == 0:
                return 2
        if data[0][0] == 0:
            return 1