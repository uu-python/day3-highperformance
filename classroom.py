class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getName(self):
        return self.firstname + " " + self.lastname

class Student(Person):
    def __init__(self, firstname, lastname, subject):
        Person.__init__(self, firstname, lastname)
        self.subject = subject
    def printNameSubject(self):
        print("%s, %s" %(self.getName(), self.subject))
    def getNameStudent(self):
        return self.getName()
        
class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
    def printNameCourse(self):
        print("%s, %s" %(self.getName(), self.course))
    def getNameTeacher(self):
        return self.getName()

def main():

    # Test the Student class
    me = Student('Benedikt', 'Daurer', 'physics')
    me.printNameSubject()

    # Test the Teacher class
    you = Teacher('Filipe', 'Maia', 'Python programming')
    you.printNameCourse()
    
if __name__ == '__main__':
    main()
    
