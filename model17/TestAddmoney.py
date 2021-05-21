import unittest
from User import User
from Bank import Bank

class Testaddmoney(unittest.TestCase):
    u=None
    b=None

    def setUp(self) -> None:
        self.u=User()
        self.b=Bank()
    def test_addmoney(self):
        #准备数据
        self.u.setAccount("12211212")
        self.u.setPassword("123")
        self.b.setMoney(1000)
        #期望结果1
        status=1
        #调方法
        statu=self.b.bank_addMoney(self.u.getAccount(),self.b.getMoney())
        #断言
        self.assertEqual(statu,status)