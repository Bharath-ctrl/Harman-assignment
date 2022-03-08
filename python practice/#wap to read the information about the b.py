#wap to read the information about the books from the user
#book name,authorname, price, publisher name

Books=[]
count=int(input())
for i in range(0,count):
    book_name=input("book name?")
    author_name=input("author name?")
    price=input("price of the book?")
    publisher_name=input("publisher name?")
    Books=[{"Book name":book_name,"Author name":author_name,"Price":price,"Publisher name":publisher_name}]
print(Books)