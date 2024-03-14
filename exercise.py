students_list = []
student_dict = {}
name = input("Enter your name here: ")
age = int(input("Enter your age here: "))
grade = int(input("enter your grade here: "))
students_list.append(name)
student_dict[name]={"age":age, "grade":grade}
print("student information added successfully!")
print(student_dict)
search_name = input("enter the name of the student to search or simply enter p to skip: ")
if search_name in students_list:
    print(f"student found! Name:{search_name},{student_dict[search_name]}")
else:
    print("student not found!")

remove_name  = input("enter the name of the studentto remove or simply enter p to skip: ")

if remove_name in students_list:
    students_list.remove(remove_name)
    del student_dict[remove_name]
    print("student has been removed successfully!")
else:
    print("student not found!")