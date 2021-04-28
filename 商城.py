'''
商城：
        1.商品
        2.薪资
        3.我的购物车
    逻辑：
        1.初始化您的薪资
        2.展示商城商品
        3.输入商品编号
        4.看钱够不够
            4.1够了，就添加我的购物车，薪资减去相对应的金额
            4.2不够，买其他的。
        继续买东西，一直到输入Q获取q，退出

'''

import  random
shop=[

    ["联想高配版",5000],
    ["iphone12高配版",3000],
    ["冰箱",1500],
    ["小米",80],
    ["不锈钢锅",100],
    ["棒棒糖",30]

]
youhuiquan=["联想优惠券","冰箱优惠券"]
a=random.choice(youhuiquan)
print(a)
jifen=0
mychart=[]
#初始化薪资
sarlary=input("请输入您的薪资")
sarlary=int(sarlary)
#直接把总金额付给salray1
sarlary1=sarlary
while True:
    #展示商品
    for  index,value in  enumerate(shop):
        print(index,"",value)
    #输入商品编号选择商品
    num=input("请输入您要购买的商品编号")
    if num.isdigit():
        num=int(num)

        if num>=len(shop):
            print("没有该商品,请重新选择编号:")
        else:  #可以买商品
            if sarlary>=shop[num][1]:
                if  shop[num][1]>=600 :
                    if  num==0  and  a=="联想优惠券":
                        sarlary=sarlary-shop[num][1]/2
                        print("成功购买商品", "薪资1剩下", sarlary)
                    elif num==1:
                        sarlary= sarlary - shop[num][1]
                        print("成功购买商品", "薪资2剩下", sarlary)
                    elif num==2  and  a=="冰箱优惠券":
                        sarlary = sarlary - shop[num][1] + 300
                        print("成功购买商品", "薪资3剩下", sarlary)
                else:
                    sarlary=sarlary-shop[num][1]
                    print("成功购买商品", "薪资4剩下", sarlary)
            else:
                print("购买商品失败","请充钱")
    elif  num=="q" or  num=="Q":
        jifen=(sarlary1-sarlary)/10
        jifen=int(jifen)
        print("退出程序，再见。欢迎您下次再来购买商品积分为",jifen)
        break
    else:
        print("输入非法")
