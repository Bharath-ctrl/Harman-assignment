#Insert into patients
import sqlite3
connection=sqlite3.connect("hospital.db")
getPID=input("Enter Patient's ID: ")
getPName=input("Enter Patient's Name: ")
getPAdd=input("Enter Patient's Address: ")
getPEmail=input("Enter Patient's Email ID: ")
getPhno=input("Enter Patient's Phone number: ")
getPPin=input("Enter Patient's Pincode: ")


connection.execute("INSERT INTO PATIENT( PATIENT_ID,PATIENT_NAME,PATIENT_ADDRESS,PATIENT_PHNO,PATIENT_EMAILID,PATIENT_PINCODE)\
                   VALUES("+getPID+",'"+getPName+"','"+getPAdd+"','"+getPEmail+"',"+getPhno+","+getPPin+")")
connection.commit()
connection.close()
print(f'Inserted Patient {getPName} details successfully')