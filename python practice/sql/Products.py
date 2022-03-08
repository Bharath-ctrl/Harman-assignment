#products db name, table name= productdata,,fields--prodcode, name, price, distributer name manufacturer name
import sqlite3
connection=sqlite3.connect("Products.db")
connection.execute('''   CREATE TABLE PRODUCTDATA(
                        PRODUCT_CODE INTEGER PRIMARY KEY AUTOINCREMENT,
                        PRODUCT_NAME TEXT,
                        PRODUCT_PRICE INTEGER,
                        DISTRIBUTER_NAME TEXT,
                        MANUFACTURER_NAME TEXT
                        );''')
print("Table created Sucessfully")
getProductName=input("Enter Product name: ")
getProductPrice=input("Enter Product Price: ")
getDistributerName=input("Enter Distributer Name: ")
getManufacturerName=input("Enter Manufacturer Name: ")

connection.execute("INSERT INTO PRODUCTDATA(PRODUCT_NAME,PRODUCT_PRICE,DISTRIBUTER_NAME,MANUFACTURER_NAME) \
     VALUES('"+getProductName+"',"+getProductPrice+",'"+getDistributerName+"','"+getManufacturerName+"')")
connection.commit()
connection.close()
print("Inserted Sucessfully")