import json

class Employee:
    def __init__(self,name,dob,height,city,state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state
def read_employee_data():
    with open('employees.json') as f:
        data = json.load(f)
    employees_data = data['employees']
    employees = []
    for employee_data in employees_data:
        employees = []
        for employee_data in employees_data:
            employee = Employee(
                employees_data['name'],
                employee_data['dob'],
                employee_data['height'],
                employee_data['city'],
                employee_data['state']
            )
            employees.append(employee)
        return employees
                
employees = read_employee_data()
for employee in employees:
    print(employee.__dict__)