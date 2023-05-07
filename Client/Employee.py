class Employee:
    id = 0
    Employees = {}
    def __init__(self, first_name, last_name, department):
        Employee.id += 1
        self.__id = Employee.id
        self.__firstName = first_name
        self.__lastName = last_name
        self.__Department = department
        print(self.__id)

    def __repr__(self):
        return f"name: {self.__firstName} {self.__lastName} department: {self.__Department}\n"

    def getID(self):
        return self.__id

    def toDict(self):
        return {"id": self.__id, "first name" : self.__firstName, "last name" : self.__lastName, "department" :
            self.__Department}
