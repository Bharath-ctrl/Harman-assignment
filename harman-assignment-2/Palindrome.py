#Palindrome number
num=int(input())#121
rev=0
temp=num
while temp>0:
    rem=temp%10
    rev=rev*10 +rem #1:rev=0->rev=1 2: rev=1*10+2=12 3: rev=12*10=120+1=121 (&temp==0.1==0)
    temp=temp//10
if rev==num:
    print("palindrome")
else:
    print("not a palindrome")
