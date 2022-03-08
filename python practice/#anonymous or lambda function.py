#anonymous or lambda function
a=12
multi=(lambda i : i**2)
m=(lambda j: j+2)
print(multi(a)+m(a))

b=int(input())
c=int(input())
d=int(input())
add= lambda u, v ,w: u+v+w
print(add(b,c,d))

#filter function takes arguments such as list and also lambda
numList=[1,2,7,89,3,4,5]
oddList=list(filter(lambda x: (x%2!=0),numList))  #using filter output=[1, 7, 89, 3, 5]
#if using map
oddList1=list(map(lambda x: (x%2!=0), numList)) #output=[True, False, True, True, True, False, True] ....It takes or considers all the items in the list
List1=list(map(lambda x: x*2, numList))      #output=[2, 4, 14, 178, 6, 8, 10]
print(oddList)
print(oddList1)
print(List1)