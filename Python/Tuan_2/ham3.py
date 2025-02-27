def Max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def TBC(a,b,c,d):
    return((a+b+c+d)/4)

a = int(input("Enter num a: "))   
b = int(input("Enter num b: "))  
c = int(input("Enter num c: "))  
d = int(input("Enter num d: "))   

print("Max la: ",Max(a,b,c))
print("TBC la: ",TBC(a,b,c,d))