#wap to check a number is divisible by 8 by using function

def isdDivisible(x):
    
    if x%8==0:
        return 'divisible'
    else:
        return 'not divisible'
a=int(input())
print(isdDivisible(a))