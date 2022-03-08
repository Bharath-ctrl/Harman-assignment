import sqlite3

connection = sqlite3.connect("hospital.db")
getPid=input("Enter Patient ID: ")

res = connection.execute(" SELECT * FROM PATIENT WHERE PATIENT_ID="+getPid)
for i in res:
    print("Normal Id",i[0])
    print("Patient ID: ", i[1])
    print("Patient Name: ", i[2])
    print("Patient Address: ", i[3])
    print(" Patient Phone number: ", i[4])
    print("Patient Email ID: ", i[5])
    print("Patient Pincode: ", i[6])
    print("*********$$$$$$***********")

