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


print(createEmpployee())
