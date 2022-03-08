#wap to create a new list which contains all the numbers which is divisible by 5 using lambda function
x=[34,56,70,89,55,3,4,5,90]
div=list(filter(lambda y: y%5==0, x))
print(div)

#wap to create a new list whcih contains the square of each items
a=[2,4,5,6,90,88]
sqr=list(map(lambda b : b*b,a))
print(sqr)

#wap to create a new list to find the square by using exponent operator
l=[2,4,5,6,90,88]
ex=list(map(lambda z : z**4,l))
print(ex)

#use of zip for tuples
a=("bharath","akash", "gani")
b=("kollur","hennuru","dommasandra")
z=zip(a,b)
print(tuple(z))

