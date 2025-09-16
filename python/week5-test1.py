#main class creation
class Student():
    def __init__(self, firstname, lastname, age, school, classroom):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self._school = school
        self.__classroom = classroom
    
    def getFirstname(self):
        return self.__firstname
    
    def getLastname(self):
        return self.__lastname
    
    def getAge(self):
        return self.__age
    
    def getSchool(self):
        return self._school
    
    def getClassroom(self):
        return self.__classroom
        
#objects creation
student_1 = Student("Ali", "KOUM", 14, "NYU", "P-4")

student_2 = Student("Bill", "ALIOUN", 19, "AIT", "SC")

#inheritance and polymorphism
class GraduatedStudent(Student):
    def __init__(self, firstname, lastname, age, school, classroom, graduation_year):
        super().__init__(firstname, lastname, age, school, classroom)
        self.__graduation_year = graduation_year

    def getSchool(self):
        return 'graduated from ' + self._school
    
    def getClassroom(self):
        return 'already graduated'
    
    def getGraduation_year(self):
        return self.__graduation_year
    
graduatedStudent = GraduatedStudent("Christ", "VALL", 21, "YUEI", "PT18", 2025)

print(student_1.getFirstname(), student_1.getLastname(), student_1.getAge(), student_1.getSchool(), student_1.getClassroom())

print(student_2.getFirstname(), student_2.getLastname(), student_2.getAge(), student_2.getSchool(), student_2.getClassroom())

print(graduatedStudent.getFirstname(), graduatedStudent.getLastname(), graduatedStudent.getAge(), graduatedStudent.getSchool(), graduatedStudent.getClassroom(), graduatedStudent.getGraduation_year())