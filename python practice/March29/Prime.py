

def prime(n):
    c = 2
    while(c*c<=n):
        if(n%c==0):
            return False
        c+=1
        if c*c>n:
            return True
        else:
            return False
if __name__ =="__main__":
    a=int(input("enter number to check Prime or not"))
    if(prime(a)):
        print(f'{a} is Prime')
    else:
        print(f'{a} is not a prime number')