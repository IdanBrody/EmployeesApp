import json

from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = "employees_dev"
app.config['MYSQL_DATABASE_PASSWORD'] = "pass12345"
app.config['MYSQL_DATABASE_DB'] = "employees"
app.config['MYSQL_DATABASE_HOST'] = "localhost"
mysql.init_app(app)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@app.route("/Home", methods=["GET", "POST"])
def home():
    return render_template('index.html')


@app.route("/test")
def test():
    return render_template('Test.html')


@app.route("/addEmployee", methods=["POST"])
def addEmployee():
    employee_data = request.get_json()
    first_name = employee_data['_Employee__firstName']
    last_name = employee_data['_Employee__lastName']
    department = employee_data['_Employee__Department']
    connection = mysql.connect()
    cursor = connection.cursor()
    query = "INSERT INTO employees (first_name, last_name, department ) VALUES (%s, %s, %s)"
    values = (first_name, last_name, department)
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return "added Employee " + str(request.json)


@app.route("/deleteEmplployee/<empID>", methods=["DELETE"])
def deleteEmployee(empID):
    connection = mysql.connect()
    cursor = connection.cursor()

    query = "DELETE FROM employees WHERE id = %s"
    values = (empID,)
    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()
    return f"Deleted employee id: {empID}"


@app.route("/EmployeesList", methods=["GET"])
def EmployeesList():
    connection = mysql.connect()
    cursor = connection.cursor()

    query = "SELECT * FROM employees"
    cursor.execute(query)
    employees = cursor.fetchall()
    emp_list = []
    for employee in employees:
        emp_list.append(employee)
    connection.close()
    cursor.close()
    return json.dumps(emp_list)

@app.route("/getByName/<first_name>", methods=["GET"])
def getEmployeeByName(first_name):
    connection = mysql.connect()
    cursor = connection.cursor()
    query = "SELECT * FROM employees WHERE first_name = %s"
    values = (first_name, )
    cursor.execute(query, values)
    employee = cursor.fetchall()
    connection.close()
    cursor.close()
    return json.dumps(employee)

@app.route("/getByID/<empID>", methods=["GET"])
def getEmployeeByID(empID):
    connection = mysql.connect()
    cursor = connection.cursor()
    query = "SELECT * FROM employees WHERE id = %s"
    values = (empID,)
    cursor.execute(query, values)
    employee = cursor.fetchall()
    connection.close()
    cursor.close()
    return json.dumps(employee)


if __name__ == "__main__":
    app.run(debug=True)
