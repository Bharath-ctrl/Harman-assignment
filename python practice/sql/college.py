import sqlite3
connection=sqlite3.connect("college.db")
getRollNumber=input("Enter the roll number:")
getName=input("Enter name:")
getAdmno=input("enter admn no:")
getCollege=input("enter college:")


#result=connection.execute("SELECT * FROM STUDENT WHERE ROLLNUMBER=" +getRollNumber)
#connection.execute("DELETE FROM STUDENT WHERE ROLLNUMBER=" +getRollNumber)
connection.execute("UPDATE STUDENT SET NAME='"+getName+"',ADMNO="+getAdmno+",COLLEGE='"+getCollege+"' WHERE ROLLNUMBER=" +getRollNumber)
connection.commit()
result=connection.execute("SELECT * FROM STUDENT ")
for i in result:
    print("id: ",i[0])
    print("name: ",i[1])
    print("rollno: ",i[2])
    print("admn no: ",i[3])
    print("college: ",i[4])