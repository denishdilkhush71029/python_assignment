class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def show_details(self):
        print(f"Student: {self.name} | Roll No: {self.roll_number} | Marks: {self.marks}")

    def check_result(self):
        if self.marks >= 33:
            return "Result: Pass"
        else:
            return "Result: Fail"

# Usage
s1 = Student("Dilkhush", 101, 75)
s1.show_details()
print(s1.check_result())
