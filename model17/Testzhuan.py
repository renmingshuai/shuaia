import  unittest
from User import User
from Bank import Bank
class  Testzhuan(unittest.TestCase):
    u=None
    u1=None
    b=None
    def setUp(self) -> None:
        self.u=User()
        self.u1=User()
        self.b = Bank()
    def test_zhuanzhang(self):

        self.u.setAccount("12211212")
        self.u1.setAccount("159359")
        self.u.setPassword("p")
        self.b.setMoney(200)

        #期望结果
        status=0
        a= self.b.bank_transfer(self.u.getAccount(),self.u1.getAccount(),self.u.getPassword(),self.b.getMoney())
        self.assertEqual(status,a)