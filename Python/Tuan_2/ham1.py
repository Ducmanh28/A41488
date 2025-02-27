def sum(a,b):
    return(a+b)
    
def minus(a,b):
    return(a-b)
    
def divide(num1, num2):
    return(num1/num2)

def mutiple(a,b):
    return(a*b)

num1 = int(input("Enter number a: "))
num2 = int(input("Enter number b: "))

print("Sum = ",sum(num1,num2))
print("Minus = ", minus(num1,num2))
print("Divide = ",divide(num1,num2))
print("Mutiple =", mutiple(num1,num2))