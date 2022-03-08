# create a new python project named hospitals....need to add patients and doctors..db name=

# add patients data to the db, normal iD,patient id,pname,address,phno,emailid,pincode
# search a patient using patient id
# view all patients

# update all the patients data wrt tp
# delet  PATIENT DATA WRT pid

# add doctors data
# CREATE A doct name, qualifi, addd,phno, emailid
# search doctor using dname
# search doctor  using phno
# view all doctors
# update the doctors data using doctors phno
# delete  DATA using doctors phno

# submit along with screenshot

import sqlite3
connection = sqlite3.connect("hospital.db")
connection.execute('''  CREATE TABLE PATIENT ( 
                        NORMAL_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        PATIENT_ID INTEGER,
                        PATIENT_NAME TEXT,
                        PATIENT_ADDRESS TEXT,PATIENT_PHNO INTEGER,PATIENT_EMAILID TEXT,PATIENT_PINCODE INTEGER
    );''')
connection.execute('''  CREATE TABLE DOCTOR ( 
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        DOCTOR_NAME TEXT,
                        DOCTOR_QUALIFICATION TEXT,
                        DOCTOR_ADDRESS TEXT,
                        DOCTOR_PHNO INTEGER,
                        DOCTOR_EMAILID TEXT
    );''')
print("Tables created successfully")
