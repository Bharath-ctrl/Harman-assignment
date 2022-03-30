def add2no(x,y):
    return x+y
def sub2no(x,y):
    return x-y
def mul2no(x,y):
    return x*y
def div2no(x,y):
    return x/y

if __name__ =="__main__":
    a=int(input("enter 1st number"))
    b=int(input("enter 2nd number"))


    sum=add2no(a,b)
    print(sum)
    diff = sub2no(a, b)
    print(diff)
    mul = mul2no(a, b)
    print(mul)
    div = div2no(a, b)
    print(div)