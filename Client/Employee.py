class Employee:
    id = 0
    Employees = {}
    def __init__(self, first_name, last_name, department):
        self.__firstName = first_name
        self.__lastName = last_name
        self.__Department = department

    def __repr__(self):
        return f"name: {self.__firstName} {self.__lastName} department: {self.__Department}\n"

    def getID(self):
        return self.__id