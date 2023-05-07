from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mySql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "employees_dev"
app.config['MYSQL_DATABASE_PASSWORD'] = "pass12345"
app.config['MYSQL_DATABASE_DB'] = "employees"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mySql.init_app(app)


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/Home", methods=["GET", "POST"])
def home():
    return render_template('Home.html')


@app.route("/test")
def test():
    connection = mySql.connect()
    return render_template('Test.html')


@app.route("/addEmployee", methods=["POST"])
def addEmployee():
    # if isinstance(employee_data, str):
    #    employee_data = json.loads(employee_data)
    # first_name = employee_data['first name']
    # last_name = employee_data['last name']
    # department = employee_data['department']
    # employee = Employee.Employee(first_name, last_name, department)
    # Employees[employee.getID()] = employee
    # print(employee.getID())
    return "added Employee " + str(request.json)


@app.route("/deleteEmplployee/<empID>", methods=["DELETE"])
def deleteEmployee(empID):
    return f"Deleted employee id: {empID}"


@app.route("/EmployeesList", methods=["GET"])
def EmployeesList():
    return "Finished"


if __name__ == "__main__":
    app.run(debug=True)
