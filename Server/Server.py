import json
from flask import Flask, render_template, request
from Employee import Employee

app = Flask(__name__, template_folder='../templates', static_folder="../static")
Employees = {}


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/Home", methods=["GET", "POST"])
def home():
    return render_template('Home.html')


@app.route("/test")
def test():
    return render_template('Test.html')


@app.route("/addEmployee", methods=["POST"])
def addEmployee():
    employee_data = request.json
    print("1")
    print(employee_data)
    if isinstance(employee_data, str):
        employee_data = json.loads(employee_data)
    print("2")
    print(employee_data)
    first_name = employee_data['first name']
    last_name = employee_data['last name']
    department = employee_data['department']
    employee = Employee.Employee(first_name, last_name, department)
    Employees[employee.getID()] = employee
    print(employee.getID())
    print(Employees)
    return "Finished"


@app.route("/EmployeesList", methods=["GET"])
def EmployeesList():
    print(Employees)
    return "Finished"


if __name__ == "__main__":
    app.run(debug=True)
