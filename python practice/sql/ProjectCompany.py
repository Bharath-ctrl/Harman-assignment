#create a new python project empCode,empName, designation, salary, company name ,mobile number to the database COMPANY
import sqlite3
connection=sqlite3.connect("Company.db")
connection.execute('''   CREATE TABLE EMPLOYEE(
                        EMPCODE INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT,
                        DESIGNATION TEXT,
                        SALARY INTEGER,
                        COMPANY_NAME TEXT,
                        MOBILENO INTEGER
                        );''')
print("Table created Sucessfully")
getName=input("Enter name: ")
getDesignation=input("Enter Designation: ")
getSalary=input("Enter Salary: ")
getCompanyName=input("Enter Company Name: ")
getMobNo=input("Enter Mobile Number: ")
connection.execute("INSERT INTO EMPLOYEE(NAME,DESIGNATION,SALARY,COMPANY_NAME,MOBILENO) \
     VALUES('"+getName+"','"+getDesignation+"',"+getSalary+",'"+getCompanyName+"',"+getMobNo+")")
connection.commit()
connection.close()
print("Inserted Sucessfully")