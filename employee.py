class Employee():
    def __init__(self,first,last,salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.total = salary
        self.salary_raise = 0

    def give_raise(self,salary_raise=5000):
        self.salary_raise += salary_raise
        self.total = self.salary + self.salary_raise
        return self.total

    def show_employee_details(self):
        print(
            "Employee First name: "+self.first.title()+
            "\nEmployee Last name: "+self.last.title()+
            "\nEmployee Salary: "+str(self.salary)+
            "\nSalary raise given: "+str(self.salary_raise)+
            "\nTotal Salary: "+str(self.total)
            )

# first = Employee('ali','ali',5000)
# first.show_employee_details()
# first.give_raise(50)
# first.show_employee_details()