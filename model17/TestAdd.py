import  unittest
from User import User
from Address import Address
from Bank import Bank


class Testadd(unittest.TestCase):
    user=None
    a=None
    b=None
    def setUp(self) -> None:
        self.user=User()
        self.a=Address()
        self.b=Bank()
    def test_add(self):
        #准备数据
        self.user.setAccount("159359")
        self.user.setUsername("n")
        self.user.setPassword("p")
        self.user.setBank("中国工商银行的昌平支行")
        self.a.setCounrry("111")
        self.a.setProvince("sd")
        self.a.setStreet("asda")
        self.a.setDoor("1199")
        #期望结果
        status=2

        statu=self.b.bank_addUser(self.user.getAccount(),self.user.getUsername(),self.user.getPassword(),self.a.getCounrry(),self.a.getProvicne(),self.a.getStreet(),self.a.getDoor())
        self.assertEqual(statu,status)

