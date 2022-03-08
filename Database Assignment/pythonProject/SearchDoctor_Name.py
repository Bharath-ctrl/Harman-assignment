import sqlite3
connection=sqlite3.connect("hospital.db")
getDName=input("Enter Doctor's Name: ")

res = connection.execute(" SELECT * FROM DOCTOR WHERE DOCTOR_NAME='"+getDName+"'")
for i in res:
    print("Id",i[0])
    print("Doctors Name: ", i[1])
    print("Doctors Qualification: ", i[2])
    print("Doctors Address: ", i[3])
    print(" Doctors Phone number: ", i[4])
    print("Doctors Email ID: ", i[5])
    print("*********$$$$$$***********")
