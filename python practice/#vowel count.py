#vowel count
vowel = 'aeiou'
c=0
name=input()
name=name.lower()
for i in name:
    for j in vowel:
        if i==j:
            c+=1
print(c)

#list consists of a range of numbers
list1=[]
n=int(input())
for i in range(1,n+1):
    list1.append(i)
print(list1)