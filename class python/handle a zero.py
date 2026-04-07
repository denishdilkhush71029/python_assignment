try:
    n = int(input("Enter numerator: "))
    d = int(input("Enter denominator: "))
    print("Result:", n / d)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")