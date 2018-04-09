class Employee:
    "Employee class represents an employee domain concept."

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        "This function is called by str(). It returns reable string of an Employee."
        return f"id: {self.id} name: {self.name}"

    def __repr__(self):
        "This function is called by repr(). It returns string representation to construct an employee."
        return f"Employee({self.id}, '{self.name}')"

class EmployeeRepository:
    "EmployeeRepository provides a collection-like interface for accessing domain objects."

    def __init__(self):
        self._employees = []

    def __iadd__(self, employee):
        "To support += for adding an employee to list."
        self._employees.append(employee)
        return self

    def __isub__(self, employee):
        "To support -= for removing an employee from list."
        self._employees.remove(employee)
        return self

    def add_employee(self, employee):
        "Add new employee if employee id is new. Otherwise, throw ValueError"
        if self.get_employee_by_id(employee.id) == None:
            self._employees.append(employee)
        else:
            raise ValueError("Duplicated employee")
        
    def find(self, employee):
        "This function finds the specified employee in Employee repository. If found, it returns the employee object. Otherwise, returns None."
        for emp in self._employees:
            if emp.id == employee.id:
                return emp
        return None

    def get_employees_by_name(self, name=""):
        "Return any employee whose name contains specified name."

        # result = []
        # for emp in self._employees:
        #     if name=="" or name.lower()==emp.name.lower():
        #         result.append(emp)
        # return result

        if len(self._employees)==0:
            raise StopIteration

        for emp in self._employees:
            if name=="" or name.lower() in emp.name.lower():
                yield emp

    def get_employee_by_id(self, id):
        "Return an employee by employee's id. None if not found."
        for emp in self._employees:
            if emp.id == id:
                return emp
        return None