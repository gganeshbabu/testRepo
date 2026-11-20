def createEmpployee():
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    employee = {
        "name": name,
        "age": age,
        "position": position
    }
    return employee


# print(createEmpployee())


def greetEmployee(employee):
    print(
        f"Hello {employee['name']}, you are {employee['age']} years old and work as a {employee['position']}.")


crtEmp = createEmpployee()

greetEmployee(crtEmp)
