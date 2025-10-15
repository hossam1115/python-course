num1=int(input("num:"))
num2=int(input("num:"))
cul=str(input("cul:"))
if cul=="+":
    print(num1+num2)
elif cul=="-":
    print(num1-num2)
elif cul=="*":
    print(num1*num2)
elif cul=="/":
    print(num1/num2)
else:
    print("error")