A=56
B=78
C=0
print("A=",A,"B=",B)
while True:
    a = input("请输入+或-:")
    if a == "+":
        C=A
        A=B
        B=C
        print("A=", A, "B=", B)
        break
    elif a == "-":
        C=B
        B=A
        A=C
        print("A=", A, "\t\tB=", B)
        break
    else:
       print("不符合")