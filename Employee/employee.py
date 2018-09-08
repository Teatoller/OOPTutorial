class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


# Create first object of Employee class
emp1 = Employee("Pally", 2000)
emp2 = Employee("Chucky", 3000)

# Add attributes
emp1.reportees = 3
emp2.reportees = 2


# Access Attributes
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
