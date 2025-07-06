def factorial(number):
    fact = number
    num = number
    while num != 1:
        fact *= num - 1
        num -= 1
    return fact

number = int(input("Enter the number you want factorial of: "))

print(f"factorial of {number} = ", factorial(number))
