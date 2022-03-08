import sqlite3
connection=sqlite3.connect("hospital.db")
getDPhno=input("Enter Doctor's Phone number: ")

getDName=input("Enter Doctor's Name: ")
getDQual=input("Enter Doctor's Qualification: ")
getDAdd=input("Enter Doctor's Address: ")
getDEmail=input("Enter Doctor's Email ID: ")
connection.execute("UPDATE DOCTOR\
                   SET DOCTOR_NAME='"+getDName+"',DOCTOR_QUALIFICATION='"+getDQual+"',DOCTOR_ADDRESS='"+getDAdd+"',DOCTOR_EMAILID='"+getDEmail+"'\
                    WHERE DOCTOR_PHNO="+getDPhno)
connection.commit()
print(f'Updated Doctor {getDName} details successfully')
res = connection.execute(" SELECT * FROM DOCTOR ")
for i in res:
    print("Id",i[0])
    print("Doctors Name: ", i[1])
    print("Doctors Qualification: ", i[2])
    print("Doctors Address: ", i[3])
    print(" Doctors Phone number: ", i[4])
    print("Doctors Email ID: ", i[5])
    print("*********$$$$$$***********")
