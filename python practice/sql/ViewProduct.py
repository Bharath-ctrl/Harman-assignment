
import sqlite3
connection=sqlite3.connect("Products.db")
# getCode=input("enter the product code:")

# getPName=input("Enter Product name:")
# getPrice=input("enter price :")
# getDname=input("enter Distributer name:")
# getMname=input("enter Manufacturer name:")

#result=connection.execute("SELECT * FROM PRODUCTDATA WHERE PRODUCT_CODE="+getCode)
#connection.execute("DELETE  FROM PRODUCTDATA WHERE PRODUCT_CODE="+getCode)
# connection.execute("UPDATE PRODUCTDATA\
#     SET PRODUCT_NAME='"+getPName+"',PRODUCT_PRICE="+getPrice+",DISTRIBUTER_NAME='"+getDname+"',MANUFACTURER_NAME='"+getMname+"' \
#     WHERE PRODUCT_CODE=" +getCode)
# connection.commit()
result=connection.execute("SELECT * FROM PRODUCTDATA")
for i in result:
    print("PRODUCT_CODE: ",i[0])
    print("PRODUCT_NAME: ",i[1])
    print("PRODUCT_PRICE: ",i[2])
    print("DISTRIBUTER_NAME: ",i[3])
    print("MANUFACTURER_NAME: ",i[4])