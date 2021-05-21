import  unittest
from User import User
from Bank import Bank
class Testqumoney(unittest.TestCase):
    u=None
    b=None
    def setUp(self) -> None:
        self.u=User()
        self.b=Bank()
    def test_qumoeny(self):
        self.u.setAccount("12211212")
        self.u.setPassword("p")
        self.b.setMoney(111)
        sta= self.b.bank_withdrawal(self.u.getAccount(),self.u.getPassword(),self.b.getMoney())
        #期望结果
        stas=0
        self.assertEqual(stas,sta)
