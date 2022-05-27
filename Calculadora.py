#Calculator with loop if you want to do another operation after one processed
def calculator():
    print("**** SIMPLE CALCULATOR WITH PYTHON ****")
    print("1. SUMA")
    print("2. SUBTRACT")
    print("3. MULTIPLY")
    print("4. DIVIDE")
    print("5. EXIT")
    operation = (input("Select an operation: "))

    if operation == "1":
        cantidad_de_num = int(input("How many numbers do you want to ADD? "))
        sum = 0
        for x in range(cantidad_de_num):
            num = int(input("Insert a number: "))
            sum = num + sum
        print("The sum result is " + str(int(sum)))
        back = input("Do you want to do another operation? (yes/no)")
        if back == "yes":
            calculator()
        else: 
            quit()

    elif operation == "2":
        cantidad_de_num = int(input("How many numbers do you want to SUBTRACT? "))
        res = 0
        for x in range(cantidad_de_num):
            num = int(input("Insert a number: "))
            res = num - res
        print("La difference result is " + str(int(res)))
        back = input("Do you want to do another operation? (yes/no)")
        if back == "yes":
            calculator()
        else: 
            quit()
    elif operation == "3":
        cantidad_de_num = int(input("How many numbers do you want to MULTIPLY? "))
        mult = 1
        for x in range(cantidad_de_num):
            num = int(input("Insert a number: "))
            mult = num * mult
        print("The product result is " + str(int(mult)))
        back = input("Do you want to do another operation? (yes/no)")
        if back == "yes":
            calculator()
        else: 
            quit()
    elif operation == "4":
        cantidad_de_num = int(input("How many numbers do you want to DIVIDE? "))
        div = 1
        for x in range(cantidad_de_num):
            num = int(input("Insert a number: "))
            div = num / div
        print("The result is " + str(int(div)))
        back = input("Do you want to do another operation? (yes/no)")
        if back == "yes":
            calculator()
        else: 
            quit()
    elif operation == "5":
        exit(); 
    else:
        print("Invalid Entry")
        calculator()

calculator();


