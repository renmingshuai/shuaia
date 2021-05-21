import  unittest
from User import User
from Bank import Bank
class  Testchaxun(unittest.TestCase):
    u = None
    b=None
    def setUp(self) -> None:
        self.u = User()
        self.b=Bank()
    def test_cha(self):
        self.u.setAccount("smhqj7a9")
        self.u.setPassword("ewq")
        #期望结果
        sta=0
        stas=self.b.bank_seek(self.u.getAccount(),self.u.getPassword())
        self.assertEqual(stas,sta)