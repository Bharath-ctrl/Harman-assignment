#wap find the sum of all the numbers from 1- 100
sum=0
for i in range(101):
    sum+=i
print(sum)

#tuple
words=("is","or",'not','or',111)
print(words)

#extras
list1=[1,2,3,4]
list2=[2,3,4]
combine=(list1+list2)
print(combine)

#dictionary
data={"name": "sun","age":"150mn"}
print(data)

#wap to read the information about the books from the user
#book name,authorname, price, publisher name
count=int(input())
Books=[]
for i in range(0,count):
    book_name=input("book name?")
    author_name=input("author name?")
    price=input("price of the book?")
    publisher_name=input("publisher name?")
    Books=[{"Book name":book_name,"Author name":author_name,"Price":price,"Publisher name":publisher_name}]
print(Books)