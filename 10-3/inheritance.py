
class Teacher(object):
    def __init__(self, Subjectname,college):
        self.Subjectname=Subjectname

        self.college=college
    def printTeacher(self):
        print("The Teacher Subject name is:",self.Subjectname)
        print("The teacher's college name is:",self.college)

class Student(Teacher):
    def __init__(self,Subjectname,college,studentname,rollno):
        self.studentname=studentname
        self.rollno=rollno
        Teacher.__init__(self,Subjectname,college)
    def printStudent(self):
        print(f'teacher subject= {self.Subjectname}\n college= {self.college} \n student name= {self.studentname} \n rollno= {self.rollno}')
subjectname=input("subject name: ")
rollno=input("roll no: ")
studentname=input("student name: ")
college=input("college: ")
stud1=Student(subjectname,college,studentname,rollno)
stud1.printStudent()
