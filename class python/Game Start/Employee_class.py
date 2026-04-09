Employee Class:
def__init__(self,name,id,salary):
    self.name = name
    self.id = id
    self.salary = salary
     def calculate_total_salary(self):
        bonus = self.salary * 0.10
        total = self.salary + bonus
        print(f"Employee: {self.name} | Bonus: {bonus} | Total Salary: {total}")

# Usage
emp = Employee("Suresh", "E001", 50000)
emp.calculate_total_salary()