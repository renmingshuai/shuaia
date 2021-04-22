

count=0
sum=0
a=0
maxx=0
while  count<10:
    count=count+1
    shu=input("请输入一个数")
    shu=int(shu)
    sum=sum+shu
    if shu>maxx:
        maxx=shu
    a=round(sum/count,2)
    print("之和为",sum,"平均数为",a,"最大数为：",maxx)
