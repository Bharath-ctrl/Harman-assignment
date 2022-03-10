#create a class student, with atrributes, name roll no. admn no, college
# #->u have to read the student information from the user and create the object aNd display the data

class Student:
    def __init__(self, name, rollno,admn_no,college):
        self.name=name
        self.rollno=rollno
        self.admn_no=admn_no
        self.college=college
    def printStudent(self):
        print("The student name is:",self.name)
        print("The student roll number is:",self.rollno)
        print("The student admission number is:",self.admn_no)
        print("The student's college name is:",self.college)


name=input()
rollno=input()
admno=input()
college=input()
stud1=Student(name,rollno,admno,college)
stud1.printStudent()