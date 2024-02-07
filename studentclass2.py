class Student:
    def __init__(self, student_id, first_name, last_name, course, year_level, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.year_level = year_level
        self.gpa = gpa

    def will_graduate(self):
        return self.year_level == 4

    def has_oop(self):
        return self.year_level == 2
    
    def is_delayed(self):
        return self.year_level >= 5
    
    def soludKlasi(self):
        self.gpa += 1
        return self.gpa

class StudentLeader(Student):
    def __init__(self,student_id, first_name, last_name, course, year_level, gpa ,orgName, position):
        StudentLeader.__init__(self, student_id, first_name, last_name, course, year_level, gpa)
        self.orgName = orgName
        self.position = position

    def will_graduate(self):
        if self.year_level == 5:
            return True
        return False
    
    def attendEvent(self):
        print("I am a representative of an " + self.orgName)

class READS(Student):
    def __init__(self, officeDuty, student_id, first_name, last_name, course, year_level, gpa):
        READS.__init__(self, student_id, first_name, last_name, course, year_level, gpa)
        self.officeDuty = officeDuty

    def will_graduate(self):
        return self.year_level == 5
    
    def duty(self):
        print("I am working at " + self.officeDuty)


def enroll_student():
    student_id = input("--Pls enter Student ID: ")
    first_name = input("--Pls enter First Name: ")
    last_name = input("--Pls enter Last Name: ")
    course = input("--Pls enter Course: ")
    year_level = int(input("--Pls enter Year Level: "))
    return Student(student_id, first_name, last_name, course, year_level)

    
def main():
    students_list = []

    while True:
        print("\n")
        print("\nMenu:")
        print("1.) Enroll Student")
        print("2.) View Student list")
        print("3.) Will student graduate?")
        print("4.) Has student taken OOP?")
        print("5.) Is student delayed?")
        print("6.) Exit")

        user_input = input("Please enter a number: ")
        number = int(user_input)
        print("\n")

        if number == 1:
            student = enroll_student()
            students_list.append(student)
            print("Student is enrolled!")
        elif number == 2:
            for student in students_list:
                print(f"ID: {student.student_id}, Name: {student.first_name} {student.last_name}, Course: {student.course}, Year Level: {student.year_level}")
        elif number == 3:
            student_id = input("Enter Student ID: ")
            for student in students_list:
                if student.student_id == student_id:
                    if student.will_graduate():
                        print("Student will graduate.")
                    else:
                        print("Student will not graduate.")
                    break
            else:
                print("Student does not exist.")
        elif number == 4:
            student_id = input("Enter Student ID: ")
            for student in students_list:
                if student.student_id == student_id:
                    if student.has_oop():
                        print("Student has taken OOP.")
                    else:
                        print("Student has not taken OOP.")
                    break
            else:
                print("Student does not exist.")
        elif number == 5:
            student_id = input("Enter Student ID: ")
            for student in students_list:
                if student.student_id == student_id:
                    if student.is_delayed():
                        print("Student is delayed.")
                    else:
                        print("Student is not delayed.")
                    break
            else:
                print("Student does not exist.")
        elif number == 6:
            print("Okay bye!")
            break    


if __name__ == "__main__":
    main()