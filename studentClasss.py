class Student:
    def __init__(self, StudentId, FirstName, LastName, Course, YearLevel):
        self.StudentId = StudentId
        self.FirstName = FirstName
        self.LastName = LastName
        self.Course = Course
        self.YearLevel = YearLevel

    @staticmethod
    def willGraduate(YearLevel):
        if YearLevel == 4:
            return True
        return False
        
    @staticmethod
    def isDelayed(YearLevel):
        if YearLevel >= 5:
            return True
        return False

    @staticmethod    
    def hasOOP(YearLevel):
        if YearLevel == 2:
            return True
        return False
    
    @staticmethod
    def enrollStudent():
        studID = input("Please enter Student ID: ")
        firstName = input("Please enter First Name: ")
        lastName = input("Please enter Last Name: ")
        course = input("Please enter Course: ")
        yearLevel = input("Please enter Year Level: ")
        s1 = Student(studID, firstName, lastName, course, yearLevel)
        return s1
        
        
def main():
    studentsList = []

    while True:
        print("\nMenu:")
        print("1.) Enroll Student")
        print("2.) View Student list")
        print("3.) Will Student graduate")
        print("4.) Does Student have OOP")
        print("5.) Exit")

        user_input = input("Please enter a number: ")
        number = int(user_input)
        ##print("You entered the number: ", number)

        if number == 1:
            s1 = Student.enrollStudent()
            studentsList.append(s1)
            print("Student is enrolled!")
        elif number == 2:
            for student in studentsList:
                print(f"ID: {student.StudentId}, Name: {student.FirstName} {student.LastName}, Course: {student.Course}, Year Level: {student.YearLevel}")
        elif number == 3:
            student_id = input("Enter Student ID: ")
            for student in studentsList:
                if student.StudentId == student_id:
                    if Student.willGraduate(int(student.YearLevel)):
                        print("Student will graduate.")
                    else:
                        print("Student will not graduate.")
                    break
            else:
                print("Student not found.")
        elif number == 4:
            student_id = input("Enter Student ID: ")
            for student in studentsList:
                if student.StudentId == student_id:
                    if Student.hasOOP(int(student.YearLevel)):
                        print("Student has taken OOP.")
                    else:
                        print("Student has not taken OOP.")
                    break
            else:
                print("Student not found.")
        elif number == 5:
            print("Exiting program...")
            break


if __name__ == "__main__":
    main()
