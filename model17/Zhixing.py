import unittest
from HTMLTestRunner import HTMLTestRunner
#创建测试集
suit=unittest.TestSuite()
#让测试加载器加载测试用例
dis=unittest.defaultTestLoader.discover(r"D:\pythonxiangmu\pythonProject\day17",pattern="Test*.py")
#将所有测试用例加载进来
suit.addTests(dis)
#创建测试运行器
f=open("测试.html",mode="w+",encoding="utf-8")
h=HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="这是我的测试",
    verbosity=2,
    description="测试用例"

)
#让运行器生成报告
h.run(suit)
