#
# wap to implemennt simple inheritance by using
# classes=student and exam...
# student shud have the prop ,,name, roll mno,admn no, college
#
# exam=exam name,eng mark, math mark, physics mark, chem mark
class Student(object):
    def __init__(self,name,rollno,admno,college):
        self.name=name
        self.rollno=rollno
        self.admno=admno
        self.college=college
class Exam(Student):
    def __init__(self,name,rollno,admno,college,english,math,physics,chemistry):
        self.english=english
        self.math=math
        self.physics=physics
        self.chemistry=chemistry
        Student.__init__(self,name,rollno,admno,college)

    def printMarksheet(self):
            print(f'Student name={name} rollno={rollno} admno={admno} college= {college}\n marks: \n EnglishMarks={english} \n Math={math} \n Physics={physics}\n Chemistry={chemistry}')
name=input("name: ")
rollno=input("rollno: ")
admno=input("admno: ")
college=input("college: ")
english=input("English marks: ")
math=input("Math marks: ")
physics=input("Physics marks: ")
chemistry=input("Chemistry marks: ")
x=Exam(name,rollno,admno,college,english,math,physics,chemistry)
x.printMarksheet()
