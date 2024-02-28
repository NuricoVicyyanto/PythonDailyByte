
print("Welcome to Basic Arithmetic App Select this operation for action \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division")
option = int(input("Select operation :"))

if option == 1:
    firstValue = int(input("Enter First Value:"))
    secondValue = int(input("Enter Second value :"))
    print("Total value is :",firstValue+secondValue)

elif option == 2:
    firstValue = int(input("Enter First Value:"))
    secondValue = int(input("Enter Second value :"))
    print("Total value is :",firstValue-secondValue)

elif option == 3:
    firstValue = int(input("Enter First Value:"))
    secondValue = int(input("Enter Second value :"))
    print("Total value is :",firstValue*secondValue)

elif option == 4:
    firstValue = int(input("Enter First Value:"))
    secondValue = int(input("Enter Second value :"))
    print("Total value is :",firstValue/secondValue)

else:
    print("Operation invalid")