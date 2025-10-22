#calculator

def add(a,b):
    sum = a + b
    return sum

def subtract(a,b):
    difference = a - b
    return difference

def multiply(a,b):
    product = a * b
    return product

def divide(a,b):
    if b == 0:
        return "Error: Division by zero is undefined."
    quotient = a / b
    return quotient

def power(a,b):
    result = a ** b
    return result

def modulus(a,b):
    remainder = a % b
    return remainder

def floor_divide(a,b):
    if b == 0:
        return "Error: Division by zero is undefined."
    floor_quotient = a // b
    return floor_quotient

#   2/5 * 4/25 = 5/2
def invert_fraction(a, b):
    if a == 0:
        return "Nie można odwrócić ułamka z licznikiem 0."
    inverted = b / a
    return inverted


def main():
    print("Calculator Module")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    option = input("Choose operation: \n1. Add \n2. Subtract \n3. multiply  \n4. divide \n5. power \n6. modulus \n7. floor_divide. \n8. interverting_fractions")

    if option == '1':
        print("Result: ", add(float(a), float(b)))
    elif option == '2':
        print("Result: ", subtract(float(a), float(b)))      
    elif option == '3':
        print("Result: ", multiply(float(a), float(b)))
    elif option == '4':
        print("Result: ", divide(float(a), float(b)))
    elif option == '5':
        print("Result: ", power(float(a), float(b)))
    elif option == '6':
        print("Result: ", modulus(float(a), float(b)))
    elif option == '7':
        print("Result: ", floor_divide(float(a), float(b)))  
    elif option == '8':
        print("Result: ", invert_fraction(float(a), float(b)))
    else:
        print("Invalid option selected.")
        
if __name__ == "__main__":
    main()

