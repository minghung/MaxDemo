from MingEmployee import *
import sys
import pickle

def select_menu():
    "This function display a menu, then returns function used to process user's selection."
    menu = [
        {"item": "[1] Add employee", "func": add_employee},
        {"item": "[2] Remove employee", "func": remove_employee},
        {"item": "[3] Display all employees", "func": display_company},
        {"item": "[4] Find employees", "func": find_employees},
        {"item": "[5] Save file", "func": save_company},
        {"item": "[6] Open file", "func": open_company},
        {"item": "[7] Exit", "func": terminate_program}
    ]

    print("\n=== Main Menu ===")
    for m in menu:
        print(m["item"])

    while True:
        try:
            selection = int(input("Enter your selection? "))

            if selection<1 or selection >len(menu):
                raise ValueError

            break
        except ValueError:
            print(f"Please enter a valid choice (from 1 to {len(menu)})!")

    return (selection, menu[selection-1]["func"])

def add_employee(company):
    "Add a new employee to company"
    id = input("New Employee Id? ")
    name = input("New Employee Name? ")
    company += Employee(id, name)

def remove_employee(company):
    "Remove an employee from company"
    display_company(company)
    id = input("Please enter employee id to remove? ")
    emp = company.get_employee_by_id(id)
    if emp != None:
        answer = input(f"Are you sure to delete {emp.name}? (Y/N)")
        if answer.lower() == "y":
            company -= emp

def display_company(company):
    "Display every employee in a company"
    print("\n=== Employee List ===")
    for emp in company.get_employees_by_name():
        print(emp)
    print("=====================")

def find_employees(company):
    name = input("Enter the name of employees that you want to find? ")
    print(f"=== Employees whose name contains {name} ===")
    for emp in company.get_employees_by_name(name):
        print(emp)
    print("=================================")

def save_company(company):
    "Save company to a file"
    filename = input("Enter filename to save? ")

    with open(filename, "wb") as f:
        pickle.dump(company, f)

def open_company(company):
    "Retore company from a file"
    filename = input("Enter filename to open? ")

    with open(filename, "rb") as f:
        return pickle.load(f)

def terminate_program(company):
    print("Thanks for using this program")
    sys.exit()

def main():
    my_company = EmployeeRepository()    

    while True:
        selection, func = select_menu()

        if selection==6:
            my_company = func(my_company)
        else:
            func(my_company)

if __name__ == "__main__":
    main()