def addition(val1,val2):
    return(val1 + val2)

def subtraction(val1,val2):
    return(val1 - val2)

def multiplication(val1,val2):
    return(val1 * val2)

def division(val1,val2):
    return(val1 / val2)

val1 = float(input("Enter the first number: "))
val2 = float(input("Enter the second number: "))

print(f"Addition:", addition(val1,val2))
print(f"Subtraction:", subtraction(val1,val2))
print(f"Multiplication:", multiplication(val1,val2))
print(f"Division:", division(val1,val2))