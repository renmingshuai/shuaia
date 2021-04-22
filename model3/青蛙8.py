
a=0
count=0
while a<20:
        a=a+3
        count=count+1
        print("第",count,"天,白天青蛙到了",a,"米")
        if a>=20:
            break
        a=a-2
        print("第", count, "天,夜里青蛙到了", a, "米")
