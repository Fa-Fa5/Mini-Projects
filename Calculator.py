#Basic Calculator
#Next step: make it into a website 
def calculator(num1,num2,op):
    if op=="1":
        return num1+num2
    elif op=="2":
        return num1-num2
    elif op=="3":
        return num1*num2
    elif op=="4":
        return "Error:Division by Zero" if num2==0 else num1/num2
    elif op=="5":
        return "Error:Modulus by Zero" if num2==0 else num1%num2
    elif op=="6":
        return num1**num2
    else:
        return ("Invalid Input")

while True:
    try:
        num1= float(input("Enter Number:"))
        num2= float(input("Enter Number:"))
    except ValueError:
        print("Invalid Number")
        continue
    op=input("Select the operation: \n " \
    "1.Add \n " \
    "2.Subtact \n " \
    "3.Multiply \n " \
    "4.Divide \n " \
    "5.Modulus \n " \
    "6.Power \n " \
    "q for Quit \n"
    "Enter choice:")
    if op=="q":
        break
    print("Result:", calculator(num1,num2,op))