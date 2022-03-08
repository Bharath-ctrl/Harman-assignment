import sqlite3
connection=sqlite3.connect("college.db")

connection.execute('''   CREATE TABLE STUDENT(
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         NAME TEXT,
                         ROLLNUMBER INTEGER,
                         ADMNO INTEGER,
                         COLLEGE TEXT
        
);''')

print("table created successfully")
getName=input("Enter name: ")
getRollNumber=input("Enter RollNumber: ")
getAdmnNo=input("Enter AdmnNo: ")
getCollege=input("Enter College: ")
connection.execute(" INSERT INTO STUDENT(NAME,ROLLNUMBER,ADMNO,COLLEGE) VALUES('"+getName+"',"+getRollNumber+","+getAdmnNo+",'"+getCollege+"')")
connection.commit()
connection.close()
print("Inserted Sucessfully")
