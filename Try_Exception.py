try:
    value = 10/0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as err:
    #print("Divide by zero")
    print(err)
except ValueError:
    print("Invalid input!")





