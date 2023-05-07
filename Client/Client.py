import requests
import json
import Employee


def printMenu():
    print("0 : testServer")
    print("1 : addEmployee")
    print("2 : getEmployeeByName")
    print("3 : getEmployeeByID")
    print("4:  getAllEmployees")
    print("5 : updateEmployee")
    print("6 : deleteEmployee")
    print("7 : importEmployeesToCSV")
    print("8 : exportEmployeesFromCSV")
    print("9 : exit")


def testServer():
    res = requests.get(url + "/test")
    print(res.status_code)

def addEmployee():
    url = 'http://127.0.0.1:5000/addEmployee'
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    department = input("Enter Department: ")
    emp = Employee.Employee(firstName, lastName, department)
    # employee_data = {
    #     'first name': firstName,
    #     'last name': lastName,
    #     'department': department
    # }
    # json_data = json.dumps(employee_data)
    response = requests.post(url, json=emp.__dict__)
    if response.status_code == 200:
        print("Employee added successfully")
    else:
        print("Error, oops", response.text)


def getEmployeeByName():
    pass


def getEmployeeByID():
    pass


def getAllEmployees():
    url = 'http://127.0.0.1:5000/EmployeesList'
    response = requests.get(url)
    print(response.text)


def updateEmployee():
    pass


def deleteEmployee():
    empID = int(input("Please insert employee's ID to delete: \n"))
    res = requests.delete(url + f'deleteEmplployee/{empID}')
    print(res.text)

def importEmployeesToCSV():
    pass


def exportEmployeesFromCSV():
    pass


def isOpen(choice, url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        print("Server isn't running")
    else:
        if response.status_code == 200:
            if choice == 0:
                return False
            return True


functions = {
    0: testServer,
    1: addEmployee,
    2: getEmployeeByName,
    3: getEmployeeByID,
    4: getAllEmployees,
    5: updateEmployee,
    6: deleteEmployee,
    7: importEmployeesToCSV,
    8: exportEmployeesFromCSV,
    9: exit
}


def main(url):
    choice = 400
    print("Welcome")
    while isOpen(choice, url):
        print(url)
        printMenu()
        choice = int(input())
        functions[choice]()


url = 'http://127.0.0.1:5000/'
main(url)
