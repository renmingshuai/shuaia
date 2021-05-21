import random

class Utils():
    def inputHelp(self, chose, datatype="str"):
        while True:
            print("请输入" + chose + ":")
            i = input(">>>")
            if len(i.strip()) == 0:
                print("该项不能为空，请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i
    # 随机生成账号
    def getRandom(self):
        # 随机生成账号
        li = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "a", "z", "w", "s", "x", "e", "d", "c", "r", "f",
              "v",
              "t", "g", "b", "y", "h", "n", "u", "j", "m", "i", "k", "o", "l", "p"]
        account = ''
        for i in range(8):
            index = random.randint(0, len(li) - 1)
            account = account + li[index]

        return account