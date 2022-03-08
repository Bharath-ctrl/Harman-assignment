import sqlite3

connection = sqlite3.connect("hospital.db")
getPid=input("Enter Patient ID: ")
getPName=input("Enter Patient's Name: ")
getPAdd=input("Enter Patient's Address: ")
getPEmail=input("Enter Patient's Email ID: ")
getPhno=input("Enter Patient's Phone number: ")
getPPin=input("Enter Patient's Pincode: ")
connection.execute("UPDATE PATIENT \
        SET PATIENT_NAME='"+getPName+"',PATIENT_ADDRESS='"+getPAdd+"',PATIENT_PHNO='"+getPEmail+"',PATIENT_EMAILID='"+getPEmail+"',PATIENT_PINCODE="+getPPin+"\
                WHERE PATIENT_ID="+getPid)
connection.commit()
print("Patient records updated")
res = connection.execute(" SELECT * FROM PATIENT")
for i in res:
    print("Normal Id",i[0])
    print("Patient ID: ", i[1])
    print("Patient Name: ", i[2])
    print("Patient Address: ", i[3])
    print(" Patient Phone number: ", i[4])
    print("Patient Email ID: ", i[5])
    print("Patient Pincode: ", i[6])
    print("*********$$$$$$***********")