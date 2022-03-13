# Create a menu-driven Python project “ Employee Management System” to manage the
# employees in a company using sqlite database.
# 1. Add the Employees ( empCode, name, phone, email, designation, salary, company
# name )
# 2. View All employees
# 3. Search an employee using employee name
# 4. Update an employee details using employee Code
# 5. Delete an employee using employee Code
# 6. Display all the details of employees whose salary is greater than 50000
# 7. Display the count of total number of employees in the company
# 8. Display all the employee details in alphabetical order, within the specific salary range
# (lower salary amount and higher amount range should be read from the user. Eg: lower
# salary range 25000 & higher salary range 60000).
# 9. Display all the employees data, whose salary is less than the average salary of all the
# employees

import sqlite3
from prettytable import PrettyTable


connection=sqlite3.connect("employee_management_system.db")
listoftables = connection.execute("select name from sqlite_master where type='table' and name = 'EMPLOYEE' ").fetchall()

if listoftables!=[]:
    print("Table already exists!")
else:

    connection.execute(''' CREATE TABLE EMPLOYEE(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    EMPCODE INTEGER,
                    NAME TEXT,
                    PHONE INTEGER,
                    EMAIL TEXT,
                    DESIGNATION TEXT,
                    SALARY INTEGER,
                    COMPANY_NAME TEXT
                    );''')
    print("Table created")

while True:
        print("Select an option from the menu given to perform the action:")
        print("1. Insert Employee data: ")
        print("2. View All employees: ")
        print("3. Search an employee using employee name :")
        print("4. Update an employee details using employee Code: ")
        print("5. Delete an employee using employee Code:")
        print("6. Display all the details of employees whose salary is greater than 50000:")
        print("7. Display the count of total number of employees in the company:")
        print("8. Display all the employee details in alphabetical order, within the specific salary range :")
        print("9. Display all the employees data, whose salary is less than the average salary of all the employee")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            getCode=input("Enter Employee Code: ")
            getName = input("Enter name: ")
            getPhone = input("Enter Phone Number: ")
            getEmail=input("Enter your email id:")
            getDesignation = input("Enter Designation: ")
            getSalary = input("Enter Salary: ")
            getCompanyName = input("Enter Company Name: ")

            result=connection.execute("INSERT INTO EMPLOYEE(EMPCODE,NAME,PHONE,EMAIL,DESIGNATION,SALARY,COMPANY_NAME) \
                 VALUES("+getCode+",'" + getName + "'," + getPhone + ",'"+getEmail+"','" + getDesignation + "'," + getSalary + ",'" + getCompanyName + "')")
            connection.commit()
            print("Inserted Sucessfully")
        elif choice == 2:
            result = connection.execute("SELECT * FROM EMPLOYEE")
            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

        elif choice == 3:
            result = connection.execute("SELECT * FROM EMPLOYEE WHERE NAME='"+getName+"'")
            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

        elif choice == 4:
            getCode = input("Enter Employee Code: ")
            getName = input("Enter name: ")
            getPhone = input("Enter Phone Number: ")
            getEmail = input("Enter your email id:")
            getDesignation = input("Enter Designation: ")
            getSalary = input("Enter Salary: ")
            getCompanyName = input("Enter Company Name: ")

            result=connection.execute("UPDATE EMPLOYEE SET NAME='"+getName+"',PHONE="+getPhone+",EMAIL='"+getEmail+"'\
                                        DESIGNATION='"+getDesignation+"',SALARY="+getSalary+",COMPANY_NAME='"+getComapny+"' WHERE EMPCODE="+getCode)
            connection.commit()

            table = PrettyTable(
                ["ID","EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7]])
            print(table)

        elif choice == 5:
            getCode = input("Enter Employee Code: ")
            result=connection.execute("DELETE FROM EMPLOYEE WHERE EMPCODE="+getCode)
            connection.commit()

            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            for i in result:
                table.add_row(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            print(table)

        elif choice == 6:
            result=connection.execute("SELECT * FROM EMPLOYEE WHERE SALARY > 50000")
            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            connection.commit()

            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

        elif choice == 7:
            result=connection.execute("SELECT COUNT(ID) AS TOTALCOUNT FROM EMPLOYEE")
            connection.commit()

            for i in result:
                print("Total count:",i[0])


        elif choice == 8:
            getFrom=input("Enter Lower Salary: ")
            getTo= input("Enter Higher Salary: ")
            result=connection.execute("SELECT * FROM EMPLOYEE WHERE SALARY BETWEEN "+ getFrom +" AND " +getTo+ " ORDER BY NAME")
            connection.commit()

            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMPANY NAME"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)

        elif choice == 9:
            result = connection.execute("SELECT * FROM EMPLOYEE WHERE SALARY < (SELECT AVG(SALARY) AS AVGSAL FROM EMPLOYEE)")
            connection.commit()
            table = PrettyTable(
                ["ID", "EMPCODE", "NAME", "PHONE", "EMAIL", "DESIGNATION", "SALARY", "COMAPANY NAME"])
            for i in result:
                table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
            print(table)
        elif choice == 10:
            connection.close()
            break

        else:
            print("Invalid choice")

