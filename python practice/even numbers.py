#wap to create a new which contains all the even numbers from 1 to 10
list1=[]
for i in range(1, 11):
    list1.append(i)
list2=[]
for i in list1:
    if(i%2==0):
        list2.append(i)
#print(list1)
#print(list2)

#wap to create a new list which contains all the numbers in between 2 and 100 which is divisible by 7
list3=[]
for i in range(2,101):
    if i%7==0:
        list3.append(i)
print(list3)

#list comprehension
#       variable i     forloop                condition
list4=[i            for i in range(1,101) if i%7==0]
print(list4)

#
new=[i.lower() for i in ['HELLO','GREEN']]
print(new)