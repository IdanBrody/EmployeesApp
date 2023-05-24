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
    print(res.text)


def addEmployee():
    url = 'http://127.0.0.1:5000/addEmployee'
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    department = input("Enter Department: ")
    emp = Employee.Employee(firstName, lastName, department)
    response = requests.post(url, json=emp.__dict__)
    if response.status_code != 200:
        print("OOPS there's an ERRORRRR\n" + response.text)


def getEmployeeByName():
    name = input("Whats the first name you want to search ? ")
    response = requests.get(url + f'/getByName/{name}')
    print(response.text)


def getEmployeeByID():
    empID = int(input("Please insert employee's ID to print: \n"))
    response = requests.get(url + f'getByID/{empID}')
    print(response.text)


def getAllEmployees():
    response = requests.get(url + "/EmployeesList")
    emp_list = json.loads(response.text)
    print("Employees list:")
    for employee in emp_list:
        print(employee)


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
        printMenu()
        choice = int(input())
        functions[choice]()


url = 'http://127.0.0.1:5000/'
main(url)
