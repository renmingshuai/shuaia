import  unittest
from  HTMLTestRunner import HTMLTestRunner
#创建测试集
su=unittest.TestSuite()
#让加载器加载你的测试用例
dis=unittest.defaultTestLoader.discover(r"D:\pythonxiangmu\pythonProject\day17",pattern="Test*.py")
#把所有测试用例加载进来
su.addTests(dis)
#创建测试运行器
f=open("qq.html",mode="w+",encoding="utf-8")
h=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="测试用例",
    verbosity=2,
    description="测试"

)
#执行
h.run(su)