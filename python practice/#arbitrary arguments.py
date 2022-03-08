#arbitrary arguments
def namesprint(*names):
    return names[0] + names[1]          
def test():
    pass
def aryt(arr):
    for i in arr:
        print(i)
arr=['hello',1,2,3,'you'] # we have to print in the function itself for dict, arr,etc any iterative
a='kil'
b='bil'
print(namesprint(a,b))
aryt(arr)

#inbuilt func
x=12.34567890
res=round(x,3) #upto 3 decimal points
print(res)

