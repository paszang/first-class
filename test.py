class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hello",self.name, "your avg marks is",sum/3)

s1 = Student("passang",[78,88,66])
s1.get_avg()