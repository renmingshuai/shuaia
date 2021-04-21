name = input("请输入您的用户名:")
age=input("请输入您的年龄")
sex=input("请输入您的性别")
sg=input("请输入您的身高")
sfzhm=input("请输入您的身份证号码")
address=input("请输入您的居住地址")
info='''   
-----------------个人信息--------------
   您的姓名：%s,
   您的年龄：%s,
   您的性别：%s,
   您的身高: %s,
   您的身份证号码：%s,
   您的居住地址: %s
 -------------------------------------
'''
print(info  % (name,age,sex,sg,sfzhm,address) )