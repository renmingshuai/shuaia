import  random
shu=random.randint(0,100)
count=0
jinbi=5000
dongjie=""
while   True:
   count=count+1
   jinbi = jinbi - 600
   a = input("请输入你要猜的数字")
   a = int(a)
   if count>=7:
       print("账户冻结不能使用退出")
       break

   if a>shu:
       print("大了")
   elif a<shu:
       print("小了")
   else:
       print("猜中了猜中的数字为",shu,"猜了",count,"次","有",jinbi,"金币")
       break