#Find the smallest number among 3 numbers using function
def smallest(x,y,z):
    return(min(x,y,z))
#or
def othersmall(x,y,z):
    if x<y and x<z:
        return x
    elif y<x and y<z:
        return y
    else:
        return z
a=int(input())
b=int(input())
c=int(input())
print(smallest(a,b,c))
print(othersmall(a,b,c))