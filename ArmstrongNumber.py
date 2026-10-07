#An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
#For example, the number 153 has 3 digits, 1**3 + 5**3 + 3**3 =153, therefore an armstrong number

def is_armstrong_number(number):
    digit_count=len(str(number)) #Len only works with string, therefore we are converting the number to str
    if digit_count==1:
        return True #All single digit numbers are armstrong numbers
    else:
        total=0
        for digit in str(number):
            digit=int(digit) #converting again into int for calculation
            digit=digit**digit_count #adding the power
            total+=digit #adding the numbers
        if number==total:
            return True
        else:
            return False
