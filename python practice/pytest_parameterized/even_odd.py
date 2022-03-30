def ChkEven(a):
    if a%2==0:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("number: "))
    print(ChkEven(a))