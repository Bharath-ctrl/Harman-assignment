#string palindrome
n=input()
rev=n[::-1]
if rev==n:
    print("palindrome")
else:
    print("Not a palindrome")
