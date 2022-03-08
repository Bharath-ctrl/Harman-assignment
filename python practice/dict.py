#wap to read the information about the books from the user
#book name,authorname, price, publisher name
Books=[]
n=int(input())
for i in range(0,n):
    book_name=input("book name?:")
    author_name=input("author name?: ")
    price=input("price of the book?: ")
    publisher_name=input("publisher name?: ")
    mybooks={"Book name":book_name,"Author name":author_name,"Price":price,"Publisher name":publisher_name}
    Books.append(mybooks)
    
#print(Books)
for i in Books:
    print(i['Book name']+i['Author name'])#this also can be done
    print(i['Author name'])