class Employee:
    def __init__(self, emp_id, name, designation, department, hours_worked, overtime_hours, deductions, salary):
        self.emp_id = emp_id
        self.name = name
        self.designation = designation
        self.department = department
        self.hours_worked = hours_worked
        self.overtime_hours = overtime_hours
        self.deductions = deductions
        self.salary = salary



    def display_info(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("Department:", self.department)
        print("Hours Worked:", self.hours_worked)
        print("Overtime Hours:", self.overtime_hours)
        print("Deductions:", self.deductions)
        print("Salary:", self.salary)
        print("Overtime Pay:", OVERTIME_PAY)
        print("Net Salary:", NET_SAL)


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def remove_employee(self, emp):
        self.employees.remove(emp)

    def calculate_payroll(self):
        print("Payroll Information")
        print("===================")
        for emp in self.employees:
            emp.display_info()
            print("-------------------")

# Create an instance of the PayrollSystem
payroll_system = PayrollSystem()

# Add employees to the payroll system
employee1 = Employee(1, "Ojerun Oritegbemi", "Manager", "Management and Ops",50,10,5000,10000)
employee2 = Employee(2, "Eyituoyo Oritseweyinmi", "Senior Developer","Software Engineering Division",70,8,400,20000)


payroll_system.add_employee(employee1)
payroll_system.add_employee(employee2)


#To capture the payroll information of a staff

add=input("Do you want to add a new user to the payroll system, YES/NO?: ")
if add == "YES":
    ID=int(input("Enter employee ID: "))
    NAME=input("Enter employee name: ")
    DESG=input("Enter employee designation: ")
    DEPT=input("Enter the employee's department: ")
    HOURS_W=float(input("Enter the number of hours worked: "))
    OVERT=float(input("Enter the number of overtime hours worked: "))
    ALAWEE=int(input("Enter employee salary: "))
    OVERTIME_PAY=OVERT * (ALAWEE / 1000)
    DEDUCT=float(input("Enter the amount for deductions: "))
    NET_SAL=ALAWEE + OVERTIME_PAY - DEDUCT

    
    
    new_employee=Employee(ID,NAME,DESG,DEPT,HOURS_W,OVERT,DEDUCT,ALAWEE)
    payroll_system.add_employee(new_employee)
    payroll_system.calculate_payroll()
else:
    # Calculate and display the payroll information
    payroll_system.calculate_payroll()
