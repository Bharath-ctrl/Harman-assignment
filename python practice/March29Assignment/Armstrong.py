def ChkArm(a):
    temp=a
    sum=0
    res=0
    while(a<=0):
        rem=a%10
        res=sum+(rem**3)
        a=a//10
    if temp==res:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("number: "))
    print(ChkArm(a))