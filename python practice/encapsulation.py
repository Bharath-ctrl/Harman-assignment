#dataEncapsulation
class School:
    def __init__(self):
        self.__marks=80     #__marks means private marks....in python we use __ instead of private
    def viewMarks(self):
        print(self.__marks)
    def Teacher(self,marks):
        self.__marks=marks

x= School()
x.viewMarks()

x.__marks=100       #cannot change datat from outside
x.viewMarks()

x.Teacher(130)
x.viewMarks()
