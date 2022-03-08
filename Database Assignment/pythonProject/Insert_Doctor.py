#Insert into patients
import sqlite3
connection=sqlite3.connect("hospital.db")
getDName=input("Enter Doctor's Name: ")
getDQual=input("Enter Doctor's Qualification: ")
getDAdd=input("Enter Doctor's Address: ")
getDPhno=input("Enter Doctor's Phone number: ")
getDEmail=input("Enter Doctor's Email ID: ")
connection.execute("INSERT INTO DOCTOR( DOCTOR_NAME,DOCTOR_QUALIFICATION,DOCTOR_ADDRESS,DOCTOR_PHNO,DOCTOR_EMAILID)\
                   VALUES('"+getDName+"','"+getDQual+"','"+getDAdd+"',"+getDPhno+",'"+getDEmail+"')")
connection.commit()
connection.close()
print(f'Inserted Doctor {getDName} details successfully')
