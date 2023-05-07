import requests
import json





def printMenu(functions):
    for key, value in functions.items():
        print(key, ":", value)


def testServer():
    url = 'http://127.0.0.1:5000/test'
    main(url)


def addEmployee():
    url = 'http://127.0.0.1:5000/addEmployee'
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    department = input("Enter Department: ")
    employee_data = {
        'first name': firstName,
        'last name': lastName,
        'department': department
    }
    json_data = json.dumps(employee_data)
    response = requests.post(url, json=json_data)
    print(json_data)
    print(response.status_code)
    print(response.text)
 #   if response.status_code == 200:
  #      print("Employee added successfully")
  #  else:
   #     print("Error, oops", response.text)


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
    pass


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
    0: "testServer",
    1: "addEmployee",
    2: "getEmployeeByName",
    3: "getEmployeeByID",
    4: "getAllEmployees",
    5: "updateEmployee",
    6: "deleteEmployee",
    7: "importEmployeesToCSV",
    8: "exportEmployeesFromCSV",
    9: "exit"
}

def switchCase(choice):
    if choice == 0:
        testServer()
    elif choice == 1:
        addEmployee()
    elif choice == 2:
        getEmployeeByName()
    elif choice == 3:
        getEmployeeByID()
    elif choice == 4:
        getAllEmployees()
    elif choice == 5:
        updateEmployee()
    elif choice == 6:
        deleteEmployee()
    elif choice == 7:
        importEmployeesToCSV()
    elif choice == 8:
        exportEmployeesFromCSV()
    elif choice == 9:
        exit(0)


def main(url):
    choice = 400
    print("Welcome")
    while isOpen(choice, url):
        print(url)
        printMenu(functions)
        choice = int(input())
        switchCase(choice)


url = 'http://127.0.0.1:5000/'
main(url)
