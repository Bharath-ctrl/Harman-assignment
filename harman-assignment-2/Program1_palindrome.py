#Palindrome 
n=int(input())
temp=n
reverse=0
while temp>0:
    rem=temp%10
    reverse=reverse*10 +(rem)
    temp=temp//10
if reverse==n:
    print("palindrome")
else:
    print("Not a palindrome")
