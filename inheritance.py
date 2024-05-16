class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number
    
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, CID Number: {self.cid_number}")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year):
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
    
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, Course: {self.course}, Year: {self.year}")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")
    
    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}, Salary: {self.salary}, Department: {self.department}, Designation: {self.designation}")

# Creating a Student object example
student = Student(name='Ram Bahadur Rai', age=20, cid_number='10304005666', student_id='02230234', course='Mechanical', year=1, )

# Creating a Teacher object example
teacher = Teacher(name='Mr.Passang', age=42, cid_number='10203005678', subject='Mathematics', salary=60000, department='Mechanical', designation='Professor')

# Displaying their information and demonstrating behaviors for a student and a teachers:
print("Student Information:")
student.display_info()
student.walk()
student.talk()
student.eat()
student.sleep()
student.study()
student.attend_class()

print("\nTeacher Information:")
teacher.display_info()
teacher.walk()
teacher.talk()
teacher.eat()
teacher.sleep()
teacher.teach()
teacher.grade_students()
teacher.attend_meeting()




     
          
    
          
          
